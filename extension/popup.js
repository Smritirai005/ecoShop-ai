document.addEventListener('DOMContentLoaded', function () {
    const checkButton = document.getElementById('checkButton');
    const brandInput = document.getElementById('brandInput');
    const resultDiv = document.getElementById('result');
  
    checkButton.addEventListener('click', function () {
      const brandName = brandInput.value;
  
      if (brandName) {
        // Call your API or function to check the brand
        checkBrand(brandName);
      } else {
        resultDiv.innerHTML = "Please enter a brand name.";
      }
    });
  
    function checkBrand(brand) {
      // Example API call to your FastAPI backend
      fetch(`http://127.0.0.1:8000/scrape-brand?brand_name=${brand}`)


        .then(response => response.json())
        .then(data => {
          if (data.score) {
            resultDiv.innerHTML = `Sustainability Score: ${data.score}`;
          } else {
            resultDiv.innerHTML = `Brand not found.`;
          }
        })
        .catch(err => {
          resultDiv.innerHTML = "Error checking brand.";
          console.error(err);
        });
    }
  });
  
  