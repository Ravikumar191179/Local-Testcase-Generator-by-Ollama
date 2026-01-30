# Project Constitution

## Data Schemas

### 1. User Input (Frontend -> Backend)
```json
{
  "user_context": "string",  // The code snippets or logic description provided by the user
  "template_type": "string"  // Optional: "unit", "integration", "e2e" (default: "unit")
}
```

### 2. Ollama Request (Backend -> Ollama API)
```json
{
  "model": "llama3.2",
  "prompt": "string", // Constructed from Template + user_context
  "stream": false,
  "options": {
    "temperature": 0.2 // Low temperature for deterministic code generation
  }
}
```

### 3. Application Output (Backend -> Frontend)
```json
{
  "test_code": "string", // The raw generated code
  "status": "success | error",
  "error_message": "string | null"
}
```

## Behavioral Rules
- **Protocol**: B.L.A.S.T protocol is law.
- **Model**: Strictly use `llama3.2`.
- **Templating**: ALL user input must be wrapped in a specific system prompt template before hitting Ollama.
- **Deterministic**: Prioritize reliability. Use low temperature settings.
- **UI**: Modern, dark-mode Chat Interface.

## Architectural Invariants
- **Backend**: Python (Flask) for routing and templating.
- **Frontend**: Vanilla HTML/CSS/JS for the Chat UI.
- **Local Only**: No external cloud calls.
## Maintenance Log
- **2026-01-30**: Initial setup using BLAST protocol. Ollama integration verified. UI built and tested.
- **V1.0.0**: Stable local generation for Unit and Integration tests using `llama3.2`.
