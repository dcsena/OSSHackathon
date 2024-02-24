# Setup
```commandline
python -m venv venv/
pip install -r requirements.txt
```

# Environment Variables
CHAT_ENDPOINT: Using Fireworks url https://api.fireworks.ai/inference/v1

CHAT_API_KEY: Using Fireworks Api Key

CHAT_MODEL: Chat Model to use

VECTARA_API_KEY: Using Vectara Personal Api key

VECTARA_CORPUS_ID: Vectara corpus for JDs

VECTARA_CUSTOMER_ID: Vectara customerId

# Run
```commandline
CHAT_ENDPOINT="https://api.fireworks.ai/inference/v1" CHAT_API_KEY={redacted} VECTARA_API_KEY={redacted} VECTARA_CORPUS_ID={redacted} VECTARA_CUSTOMER_ID={redacted} python3 vectara_upload.py
```