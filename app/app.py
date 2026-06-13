from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    data = pd.DataFrame([{
        "Product_Category": request.form['Product_Category'],
        "Product_Price": float(request.form['Product_Price']),
        "Order_Quantity": int(request.form['Order_Quantity']),
        "User_Age": int(request.form['User_Age']),
        "User_Gender": request.form['User_Gender'],
        "User_Location": request.form['User_Location'],
        "Payment_Method": request.form['Payment_Method'],
        "Shipping_Method": request.form['Shipping_Method'],
        "Discount_Applied": float(request.form['Discount_Applied'])
    }])

    prediction = model.predict(data)[0]

    return render_template(
        'index.html',
        prediction_text=f"Prediction : {prediction}"
    )

if __name__ == "__main__":
    app.run(debug=True)