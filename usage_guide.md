# Usage Guide - Testcase Generator

## 🛠 Prerequisites
- **Ollama**: Ensure Ollama is installed and running.
- **Model**: Pull the llama3.2 model: `ollama pull llama3.2`.
- **Python**: Python 3.9+ recommended.
- **Dependencies**: Install via `pip install -r requirements.txt`.

## 🚀 Running the App
1. Navigate to the project directory.
2. Run the server: `python3 app.py`.
3. Open your browser and go to `http://localhost:5001`.

## 🧪 How to Generate Tests
1. **Select Template**: Choose between "Unit Tests" or "Integration Tests".
2. **Input Context**: Paste a code snippet (e.g., a Python function) or describe the logic you want to test.
3. **Generate**: Click the "Generate Tests" button.
4. **Copy**: Use the copy icon in the output panel to grab the generated code.

## 📁 Project Structure
- `app.py`: The Flask server.
- `tools/`: Core logic for Ollama interaction.
- `architecture/`: Prompt engineering strategy and templates.
- `static/`: Frontend assets (HTML, CSS, JS).

## 🔒 Security & Privacy
This application runs **100% locally**. No data is sent to external clouds or third-party servers.
