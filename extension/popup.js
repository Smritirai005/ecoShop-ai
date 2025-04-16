document.getElementById('checkBtn').addEventListener('click', async () => {
    const brand = document.getElementById('brandInput').value;
    const resultDiv = document.getElementById('result');
  
    if (!brand) {
      resultDiv.textContent = 'Please enter a brand name.';
      return;
    }
  
    try {
      const response = await fetch("http://127.0.0.1:8000/score", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ brand_name: brand })
      });
  
      if (!response.ok) throw new Error("API error");
  
      const data = await response.json();
  
      resultDiv.innerHTML = `
        <strong>${data.brand}</strong><br>
        Score: ${data.score}/100<br>
        ${data.summary}
      `;
    } catch (error) {
      resultDiv.textContent = "Something went wrong. Is your backend running?";
    }
  });
  
  