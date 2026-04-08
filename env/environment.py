import copy
from .models import Observation, Action, Reward, VisibleEmail
from .tasks import TASKS

class EmailTriageEnv:
    def __init__(self, task="easy"):
        self.task = task
        self.reset()

    def reset(self):
        data = TASKS[self.task]
        self.emails = copy.deepcopy(data["emails"])
        self.time = data["time_remaining"]
        return self.state()

    def state(self):
        visible = [
            VisibleEmail(id=e.id, subject=e.subject, content=e.content, handled=e.handled)
            for e in self.emails
        ]
        return Observation(emails=visible, time_remaining=self.time)

    def step(self, action: Action):
        reward = 0.0

        for e in self.emails:
            if e.id == action.email_id and not e.handled:

                if action.action_type == "classify":
                    if action.priority == e.true_priority:
                        reward += 0.2
                    else:
                        reward -= 0.1
                    e.handled = True

                elif action.action_type == "respond":
                    reward += 0.4
                    e.handled = True

                elif action.action_type == "ignore":
                    if e.true_priority == "high":
                        reward -= 0.5
                    else:
                        reward += 0.1
                    e.handled = True

                elif action.action_type == "schedule":
                    reward += 0.2
                    e.handled = True

        self.time -= 1
        done = self.time <= 0 or all(e.handled for e in self.emails)

        return self.state(), Reward(value=reward), done, {}