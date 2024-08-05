from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage as MistralChatMessage
import openai
from dotenv import load_dotenv
import os
import subprocess
import sys

load_dotenv()

def call_small_model(prompt: str) -> str:
    client = openai.OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        timeout=100,
    )
    model = "huggingfaceh4/zephyr-7b-beta:free"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    response = response.choices[0].message.content
    return response


def open_file_with_default(filename):
    try:
        if sys.platform.startswith('darwin'):  # macOS
            subprocess.call(['open', filename])
        elif sys.platform.startswith('win'):  # Windows
            subprocess.call(['start', filename], shell=True)
        elif sys.platform.startswith('linux'):  # Linux
            subprocess.call(['xdg-open', filename])
        else:
            print("Unsupported platform")
    except Exception as e:
        print(f"Failed to open file: {e}")
