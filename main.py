import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    #grabs API key from .env and declares error if no key found
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("No API key found")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages,
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if response.usage_metadata == None:
        raise RuntimeError("Failed API request. Please try again.")

    if args.verbose:
        print(
            f"User prompt: {prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}"
            )
    print("Response:")
    print(response.text)



if __name__ == "__main__":
    main()
