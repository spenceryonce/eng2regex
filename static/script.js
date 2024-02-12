document.addEventListener("DOMContentLoaded", function() {
    const generateBtn = document.getElementById("generateBtn");
    const regexOutput = document.getElementById("regexOutput");

    generateBtn.addEventListener("click", function() {
        const englishInput = document.getElementById("englishInput").value;
        const exampleText = document.getElementById("exampleText").value;
        const exampleResultText = document.getElementById("exampleResultText").value;

        fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                englishInput: englishInput,
                exampleText: exampleText,
                exampleResultText: exampleResultText,
            }),
        })
        .then(response => response.json())
        .then(data => {
            regexOutput.textContent = data.regex;
        })
        .catch(error => {
            console.error("Error:", error);
            regexOutput.textContent = "Failed to generate regex. Please try again.";
        });
    });
});
