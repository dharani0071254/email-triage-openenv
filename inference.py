import os
from openai import OpenAI
from env.environment import EmailTriageEnv
from env.models import Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.getenv("HF_TOKEN", "dummy")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

env = EmailTriageEnv("easy")

print(f"[START] task=easy env=openenv model={MODEL_NAME}")

obs = env.reset()
rewards = []
steps = 0

try:
    while True:
        steps += 1

        email = obs.emails[0]

        action = Action(
            action_type="respond",
            email_id=email.id,
            message="ok"
        )

        obs, reward, done, _ = env.step(action)
        rewards.append(reward.value)

        print(f"[STEP] step={steps} action=respond({email.id}) reward={reward.value:.2f} done={str(done).lower()} error=null")

        if done:
            break

    score = min(max(sum(rewards)/10, 0.0), 1.0)
    success = score > 0.1

finally:
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={','.join([f'{r:.2f}' for r in rewards])}")