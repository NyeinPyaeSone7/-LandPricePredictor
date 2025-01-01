from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Land area (sq. ft.) and price ($) data
x = np.array([120, 430, 550, 220, 350, 700, 410, 800, 150, 900, 600, 500, 
              950, 320, 750, 800, 100, 600, 300, 400, 650, 550, 700, 480, 
              850, 500, 600, 200, 650])
y = np.array([5500, 6800, 7200, 6000, 8500, 12000, 7800, 13500, 5000, 14000, 
              10500, 9000, 14500, 7500, 13000, 14200, 5200, 10800, 7200, 8500, 
              11500, 9800, 12800, 8200, 14100, 9300, 10200, 6100, 11000])

# Calculate the slope (m) and intercept (b) for the linear regression
n = len(x)
m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y) - m * np.sum(x)) / n

@app.route("/", methods=["GET", "POST"])
def index():
    price = None
    if request.method == "POST":
        try:
            land_area = float(request.form["land_area"])
            # Calculate the price using the linear regression formula
            price = m * land_area + b
        except ValueError:
            price = "Invalid input! Please enter a valid number."
    
    return render_template("index.html", price=price)

if __name__ == "__main__":
    app.run(debug=True)