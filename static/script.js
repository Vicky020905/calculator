const display = document.getElementById('display');

function appendToDisplay(value) {
    display.textContent += value;
}

function clearDisplay() {
    display.textContent = '';
}

function deleteLast() {
    display.textContent = display.textContent.slice(0, -1);
}

async function calculateResult() {
    const expression = display.textContent;
    const response = await fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `expression=${encodeURIComponent(expression)}`,
    });
    const data = await response.json();
    display.textContent = data.result;
}
