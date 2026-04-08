from fastapi import FastAPI
from env.environment import EmailTriageEnv

app = FastAPI()

env = EmailTriageEnv("easy")

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs.model_dump()
    }

@app.get("/reset")
def reset_get():
    obs = env.reset()
    return {
        "observation": obs.model_dump()
    }

@app.post("/step")
def step(action: dict):
    from env.models import Action
    action_obj = Action(**action)

    obs, reward, done, info = env.step(action_obj)

    return {
        "observation": obs.model_dump(),
        "reward": reward.value,
        "done": done,
        "info": info
    }