# Ecommerce Return Prediction System

## Project Overview

The Ecommerce Return Prediction System is a Machine Learning-based web application that predicts whether a product purchased through an e-commerce platform is likely to be returned by the customer. The system helps businesses reduce operational costs, improve customer satisfaction, and optimize inventory management.

---

## Problem Statement

Product returns are a major challenge for e-commerce companies. High return rates increase logistics costs, affect inventory planning, and reduce profitability.

This project aims to predict the probability of product returns using historical customer and order data, enabling businesses to take preventive actions and improve decision-making.

---

## Dataset

The dataset contains information related to:

- Customer details
- Product information
- Order history
- Purchase behavior
- Return status

### Features Used

- Customer ID
- Product Category
- Purchase Amount
- Order Quantity
- Payment Method
- Delivery Details
- Previous Return History
- Customer Rating

### Target Variable

- Returned (Yes/No)

---

## Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

### Web Framework
- Flask

### Development Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

## Project Architecture

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Serialization (.pkl)
   ↓
Flask Web Application
   ↓
Prediction Output
```

---

## Machine Learning Model

The project uses Machine Learning algorithms to classify whether an order is likely to be returned.

### Steps Performed

1. Data Cleaning
2. Handling Missing Values
3. Feature Encoding
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Prediction Generation

---

## Model Performance

### Accuracy

**Accuracy: 80%+**

> Replace XX with your actual model accuracy.

### Evaluation Metrics

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Features

- Predict product return likelihood
- User-friendly web interface
- Fast prediction results
- Machine Learning-based decision support
- Scalable architecture

---

## Screenshots

### Home Page
Add screenshot here

### Prediction Page
Add screenshot here

### Result Page
Add screenshot here

---

## Installation Steps

### Clone Repository

```bash
git clone https://github.com/anchal-pal/ecommerce-return-prediction-system.git
```

### Navigate to Project Folder

```bash
cd ecommerce-return-prediction-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Future Improvements

- Deploy on AWS/Azure
- Real-time prediction API
- Advanced ML models
- Interactive dashboard
- Return probability visualization
- Customer behavior analytics

---

## Project Outcomes

- Reduced manual analysis effort
- Improved return prediction accuracy
- Better inventory management support
- Data-driven business decisions

---

## Author

**Anchal Pal**

BCA (Cloud & Cyber Security)
IIMT University, Meerut

GitHub:
https://github.com/anchal-pal

---

## License

This project is developed for educational and learning purposes.
