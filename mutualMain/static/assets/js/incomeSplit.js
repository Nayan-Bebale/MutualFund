function calculate() {
    const income = parseFloat(document.getElementById('income').value);
    if (isNaN(income) || income <= 0) {
        alert('Please enter a valid income amount.');
        return;
    }

    const needs = income * 0.5;
    const wants = income * 0.3;
    const savings = income * 0.2;

    const lowRiskInvestment = savings * 0.9;
    const highRiskInvestment = savings * 0.1;

    const results = `
        <h3>Income Allocation</h3>
        <p>Needs: ₹${needs.toFixed(2)}</p>
        <p>Wants: ₹${wants.toFixed(2)}</p>
        <p>Savings: ₹${savings.toFixed(2)}</p>
        <h3>Savings Allocation</h3>
        <p>Low Risk Investment: ₹${lowRiskInvestment.toFixed(2)}</p>
        <p>High Risk Investment: ₹${highRiskInvestment.toFixed(2)}</p>
    `;

    document.getElementById('results').innerHTML = results;
}
