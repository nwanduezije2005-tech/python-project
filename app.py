# SmartPlate Project
# Ezijie Nwandu
# Purpose: Automate plate tracking and billing
# for conveyor belt sushi restaurants

from flask import Flask

app = Flask(__name__)

# Sample sushi plate data
plates = [
    {"type": "Salmon Roll", "price": 5},
    {"type": "Tuna Roll", "price": 6},
    {"type": "Shrimp Tempura", "price": 7}
]

# Home page
@app.route('/')
def home():
    return """
    <h1>Welcome to SmartPlate</h1>
    <p>A smart restaurant billing system for conveyor belt sushi restaurants.</p>
    <p>Use /bill to view the customer bill.</p>
    """

# Billing page
@app.route('/bill')
def bill():

    total = 0

    bill_output = "<h1>Customer Bill</h1>"

    for plate in plates:
        bill_output += f"<p>{plate['type']} - ${plate['price']}</p>"
        total += plate['price']

    bill_output += f"<h2>Total: ${total}</h2>"

    return bill_output


# About page
@app.route('/about')
def about():
    return """
    <h1>About SmartPlate</h1>
    <p>This project was designed using Python and Flask.</p>
    <p>The goal is to automate restaurant plate tracking and billing.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
