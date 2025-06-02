import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Step 1: Load data from CSV
df = pd.read_csv("talent_demand_data.csv")
df["Month"] = pd.to_datetime(df["Month"])

# Step 2: Add numeric feature for months
df["Month_Num"] = np.arange(len(df))
X = df[["Month_Num"]]
y = df["Demand"]

# Step 3: Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Forecast next 6 months
future_months = pd.date_range(start=df["Month"].max() + pd.DateOffset(months=1), periods=6, freq="MS")
future_df = pd.DataFrame({
    "Month_Num": np.arange(len(df), len(df) + 6),
    "Month": future_months
})
future_df["Predicted_Demand"] = model.predict(future_df[["Month_Num"]])

# Step 5: Plot
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Demand"], marker='o', label="Actual Demand")
plt.plot(future_df["Month"], future_df["Predicted_Demand"], marker='x', linestyle='--', color='green', label="Forecast")
plt.title("Talent Demand Forecast from Real CSV Data")
plt.xlabel("Month")
plt.ylabel("Headcount Required")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
