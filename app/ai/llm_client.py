import openai
from app.config import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY


class LLMClient:
    def generate(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content
