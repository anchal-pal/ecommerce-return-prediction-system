import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/ecommerce_returns_synthetic_data.csv")

df = df[[
    'Product_Category',
    'Product_Price',
    'Order_Quantity',
    'User_Age',
    'User_Gender',
    'User_Location',
    'Payment_Method',
    'Shipping_Method',
    'Discount_Applied',
    'Return_Status'
]]

X = df.drop("Return_Status", axis=1)

y = df["Return_Status"]

categorical_features = [
    'Product_Category',
    'User_Gender',
    'User_Location',
    'Payment_Method',
    'Shipping_Method'
]

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'),
         categorical_features)
    ],
    remainder='passthrough'
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

joblib.dump(pipeline, "model/model.pkl")

print("Model Saved Successfully")