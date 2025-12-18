async function checkNews() {
    const text = document.getElementById('newsInput').value;
    const resultDiv = document.getElementById('result');
    const loader = document.getElementById('loader');
    const btn = document.getElementById('predictBtn');
    
    if (!text.trim()) { 
        alert("Please enter some text"); 
        return; 
    }

    resultDiv.style.display = 'none';
    loader.style.display = 'block';
    btn.disabled = true;

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        
        loader.style.display = 'none';
        btn.disabled = false;
        resultDiv.style.display = 'block';
        resultDiv.className = data.prediction; 
        resultDiv.innerHTML = `Result: ${data.prediction} <br> Confidence: ${(data.confidence * 100).toFixed(2)}%`;
    } catch (error) {
        loader.style.display = 'none';
        btn.disabled = false;
        resultDiv.style.display = 'block';
        resultDiv.innerText = "Error connecting to server.";
    }
}