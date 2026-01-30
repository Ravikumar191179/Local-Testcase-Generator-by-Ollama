import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def test_connection():
    print(f"🔗 Testing connection to Ollama ({OLLAMA_URL})...")
    payload = {
        "model": MODEL,
        "prompt": "Hello",
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=10)
        response.raise_for_status()
        print("✅ Connection Successful!")
        print(f"📡 Response Code: {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return False

if __name__ == "__main__":
    test_connection()
