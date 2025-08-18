import pandas as pd

# Data Extract
raw_sales = pd.DataFrame({
    "order_id": [1,2,3,4,5],
    "customer_id": [101,102,103,104,105],
    "product": ["Laptop","Mouse","Keyboard","Monitor","Headset"],
    "quantity": [1,2,1,1,3],
    "price": [3500,50,150,1200,200],
    "date": ["2024-01-12","2024-01-13","2024-01-14","2024-01-15","2024-01-16"]
})
raw_sales.to_csv("01_data-extract/raw_sales.csv", index=False)

# Data Cleaning
raw_sales["total"] = raw_sales["quantity"] * raw_sales["price"]
raw_sales.to_csv("02_data-cleaning/sales_cleaned.csv", index=False)

# Customer Profile
customer_profile = pd.DataFrame({
    "customer_id": [101,102,103,104,105],
    "age": [34,28,40,23,37],
    "gender": ["M","F","M","F","M"],
    "region": ["South","North","East","West","South"],
    "total_spent": [3500,100,150,1200,600]
})
customer_profile.to_csv("03_exploratory-analysis/customer_profile.csv", index=False)

# Train & Test for Modeling
train = customer_profile.copy()
train["churn"] = [0,1,1,0,0]
train.to_csv("04_modeling/train.csv", index=False)

test = pd.DataFrame({
    "customer_id": [106,107,108],
    "age": [29,42,31],
    "gender": ["F","M","F"],
    "region": ["North","East","West"],
    "total_spent": [800,2000,450]
})
test.to_csv("04_modeling/test.csv", index=False)

# Predictions
preds = pd.DataFrame({
    "customer_id": [106,107,108],
    "churn_probability": [0.15,0.80,0.30]
})
preds.to_csv("05_deployment/prediction_results.csv", index=False)
