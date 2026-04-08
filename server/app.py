from fastapi import FastAPI
from env.environment import EmailTriageEnv

app = FastAPI()
env = EmailTriageEnv("easy")

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs.model_dump()}

@app.post("/step")
def step(action: dict):
    from env.models import Action
    action_obj = Action(**action)
    obs, reward, done, _ = env.step(action_obj)

    return {
        "observation": obs.model_dump(),
        "reward": reward.value,
        "done": done
    }
    def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
