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
            // Convert the regex to Markdown formatted text
            const markdown = data.regex;
            // Use marked.js to convert Markdown to HTML
            const html = marked(markdown, {
                highlight: function(code, lang) {
                    return hljs.highlight(code, {language: lang}).value;
                }
            });
            // Set the innerHTML of the regexOutput element to the highlighted HTML
            regexOutput.innerHTML = html;
        })
        
        .catch(error => {
            console.error("Error:", error);
            regexOutput.textContent = "Failed to generate regex. Please try again.";
        });
    });

    
});
