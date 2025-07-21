# Gemini API Key
Get the API key from Google AI Studio: https://aistudio.google.com and set the environment variable

```sh
export GOOGLE_API_KEY="your-api-key"
```

# Execution
Start the python virtual environment and install the dependencies

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the program with a prompt

```sh
python gemini.py "explain what is ai in brief"
```
