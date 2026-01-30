import requests
import json
import sys

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def get_template(user_context):
    """
    Constructs the prompt based on the refined strategy.
    Reference: architecture/prompt_engineering.md
    """
    return f"""You are an expert QA Automation Engineer.
Your task is to generate comprehensive Test Cases for the following logic or code:

<USER_CONTEXT>
{user_context}
</USER_CONTEXT>

**Requirements:**
1. Generate test cases covering:
   - Happy Paths
   - Edge Cases
   - Negative Scenarios
2. Use standard automation frameworks (e.g., Pytest, Selenium, Playwright) if applicable based on context.
3. Provide a clear structure: Test Name, Steps, Expected Result.
4. If code is provided, generate the actual test code.
5. Return ONLY the markdown formatted test cases or code.
"""

def generate_test_case(user_context, template_type="default"):
    """
    Generates test cases using Ollama.
    """
    prompt = get_template(user_context)
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return {
            "status": "success",
            "test_code": data.get("response", "")
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e)
        }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        context = sys.argv[1]
        print(json.dumps(generate_test_case(context), indent=2))
    else:
        print("Usage: python3 tools/generate_test_case.py <context>")
