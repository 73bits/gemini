import os
import sys
from google import genai

def main() -> None:
    if len(sys.argv) == 2:
        prompt: str = sys.argv[1]
        try:
            client = genai.Client(api_key = os.getenv('GOOGLE_API_KEY'))
            response = client.models.generate_content(model = 'gemini-2.5-flash', contents = prompt)
            print(response.text.replace("**", "").replace("`", ""))
            sys.exit(0)
        except Exception as e:
            print(e)
    else:
        print("error: require one prompt")
        sys.exit(1)
    return None

if __name__ == "__main__":
    main()
