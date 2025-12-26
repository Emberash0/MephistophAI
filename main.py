import os
from dotenv import load_dotenv
from google import genai


def main():
    #grabs API key from .env and declares error if no key found
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("No API key found")

if __name__ == "__main__":
    main()
