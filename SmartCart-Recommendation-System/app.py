from flask import Flask, render_template, request
from recommendation import recommend
import pandas as pd

app = Flask(__name__)

# Load products
data = pd.read_csv("products.csv")
product_list = data['name'].tolist()

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        selected_product = request.form["product"]

        recommendations = recommend(selected_product)

    return render_template(
        "index.html",
        products=product_list,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
