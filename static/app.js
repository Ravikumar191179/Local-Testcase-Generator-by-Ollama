document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generateBtn');
    const userInput = document.getElementById('userInput');
    const outputCode = document.getElementById('outputCode');
    const templateSelect = document.getElementById('templateDocs');
    const btnText = generateBtn.querySelector('.btn-text');
    const spinner = generateBtn.querySelector('.spinner');

    generateBtn.addEventListener('click', async () => {
        const text = userInput.value.trim();
        if (!text) return;

        // UI Loading State
        setLoading(true);
        outputCode.innerText = "Generating test cases with Llama 3.2...";
        outputCode.style.color = "#9ca3af";

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_context: text,
                    template_type: templateSelect.value
                })
            });

            const data = await response.json();

            if (data.status === 'success') {
                outputCode.innerText = data.test_code;
                outputCode.style.color = "#a7f3d0"; // Success text color
            } else {
                outputCode.innerText = "Error: " + (data.error_message || "Unknown error");
                outputCode.style.color = "#fca5a5"; // Error color
            }

        } catch (error) {
            outputCode.innerText = "Network Error: " + error.message;
            outputCode.style.color = "#fca5a5";
        } finally {
            setLoading(false);
        }
    });

    function setLoading(isLoading) {
        if (isLoading) {
            btnText.style.visibility = 'hidden';
            spinner.style.display = 'block';
            generateBtn.disabled = true;
            generateBtn.style.opacity = '0.7';
        } else {
            btnText.style.visibility = 'visible';
            spinner.style.display = 'none';
            generateBtn.disabled = false;
            generateBtn.style.opacity = '1';
        }
    }

    // Copy to clipboard
    document.getElementById('copyBtn').addEventListener('click', () => {
        const code = outputCode.innerText;
        navigator.clipboard.writeText(code).then(() => {
            alert('Copied to clipboard!');
        });
    });
});
