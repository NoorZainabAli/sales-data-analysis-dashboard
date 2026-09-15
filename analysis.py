
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# ============================================================
# SALES DATA ANALYSIS & VISUALIZATION PROJECT
# ============================================================

print("=" * 70)
print("SALES DATA ANALYSIS & VISUALIZATION")
print("=" * 70)

os.makedirs("visualizations", exist_ok=True)


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("sales_data.csv")

print("\n===== DATASET =====")
print(df)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== LAST 5 ROWS =====")
print(df.tail())


# ============================================================
# 2. BASIC DATASET INFORMATION
# ============================================================

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATASET INFORMATION =====")
df.info()

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())


# ============================================================
# 3. DATA QUALITY CHECK
# ============================================================

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicate rows removed successfully.")


# ============================================================
# 4. DATA PREPROCESSING
# ============================================================

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month_name()

month_order = [
    "January",
    "February",
    "March",
    "April",
    "May"
]

df["Month"] = pd.Categorical(
    df["Month"],
    categories=month_order,
    ordered=True
)

df["Profit"] = df["Sales"] - df["Cost"]

print("\n===== PREPROCESSED DATA =====")
print(df.head())


# ============================================================
# 5. OVERALL PERFORMANCE
# ============================================================

total_sales = df["Sales"].sum()
total_cost = df["Cost"].sum()
total_profit = df["Profit"].sum()

profit_margin = (total_profit / total_sales) * 100

print("\n===== OVERALL PERFORMANCE =====")
print("Total Sales:", total_sales)
print("Total Cost:", total_cost)
print("Total Profit:", total_profit)
print("Overall Profit Margin: {:.2f}%".format(profit_margin))


# ============================================================
# 6. MONTHLY SALES
# ============================================================

monthly_sales = df.groupby(
    "Month",
    observed=False
)["Sales"].sum()

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()

plt.savefig("visualizations/monthly_sales.png")
plt.show()


# ============================================================
# 7. MONTHLY PROFIT
# ============================================================

monthly_profit = df.groupby(
    "Month",
    observed=False
)["Profit"].sum()

print("\n===== MONTHLY PROFIT =====")
print(monthly_profit)

plt.figure(figsize=(8, 5))
monthly_profit.plot(kind="bar")

plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/monthly_profit.png")
plt.show()


# ============================================================
# 8. PRODUCT-WISE SALES
# ============================================================

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PRODUCT-WISE SALES =====")
print(product_sales)

plt.figure(figsize=(10, 5))
product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visualizations/product_sales.png")
plt.show()


# ============================================================
# 9. PRODUCT-WISE PROFIT
# ============================================================

product_profit = (
    df.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PRODUCT-WISE PROFIT =====")
print(product_profit)

plt.figure(figsize=(10, 5))
product_profit.plot(kind="bar")

plt.title("Product-wise Profit")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visualizations/product_profit.png")
plt.show()


# ============================================================
# 10. TOP 5 PRODUCTS BY SALES
# ============================================================

top_5_products = product_sales.head(5)

print("\n===== TOP 5 PRODUCTS BY SALES =====")
print(top_5_products)

plt.figure(figsize=(8, 5))
top_5_products.plot(kind="bar")

plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visualizations/top_5_products.png")
plt.show()


# ============================================================
# 11. CATEGORY-WISE SALES
# ============================================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== CATEGORY-WISE SALES =====")
print(category_sales)

plt.figure(figsize=(6, 6))

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Category-wise Sales")
plt.ylabel("")
plt.tight_layout()

plt.savefig("visualizations/category_sales.png")
plt.show()


# ============================================================
# 12. CATEGORY-WISE PROFIT
# ============================================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== CATEGORY-WISE PROFIT =====")
print(category_profit)

plt.figure(figsize=(7, 5))
category_profit.plot(kind="bar")

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/category_profit.png")
plt.show()


# ============================================================
# 13. CATEGORY-WISE PROFIT MARGIN
# ============================================================

category_summary = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

category_summary["Profit_Margin"] = (
    category_summary["Profit"] /
    category_summary["Sales"]
) * 100

print("\n===== CATEGORY-WISE PROFIT MARGIN =====")
print(category_summary)

plt.figure(figsize=(7, 5))

category_summary["Profit_Margin"].plot(kind="bar")

plt.title("Profit Margin by Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/category_profit_margin.png")
plt.show()


# ============================================================
# 14. CATEGORY SALES VS PROFIT
# ============================================================

category_comparison = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

print("\n===== CATEGORY SALES VS PROFIT =====")
print(category_comparison)

category_comparison.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Category-wise Sales vs Profit")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.legend()

plt.tight_layout()

plt.savefig("visualizations/category_sales_vs_profit.png")
plt.show()


# ============================================================
# 15. REGION-WISE SALES
# ============================================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== REGION-WISE SALES =====")
print(region_sales)

plt.figure(figsize=(7, 5))

region_sales.plot(kind="bar")

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/region_sales.png")
plt.show()


# ============================================================
# 16. REGION-WISE PROFIT
# ============================================================

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== REGION-WISE PROFIT =====")
print(region_profit)

plt.figure(figsize=(7, 5))

region_profit.plot(kind="bar")

plt.title("Region-wise Profit")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/region_profit.png")
plt.show()


# ============================================================
# 17. SALES VS QUANTITY
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Quantity"],
    df["Sales"]
)

plt.title("Sales vs Quantity")
plt.xlabel("Quantity Sold")
plt.ylabel("Sales")
plt.grid(True)

plt.tight_layout()

plt.savefig("visualizations/sales_quantity.png")
plt.show()


# ============================================================
# 18. PROFIT DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Profit"],
    bins=6
)

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Number of Products")
plt.grid(True)

plt.tight_layout()

plt.savefig("visualizations/profit_distribution.png")
plt.show()


# ============================================================
# 19. BUSINESS INSIGHTS
# ============================================================

best_sales_product = product_sales.idxmax()
best_profit_product = product_profit.idxmax()
best_sales_category = category_sales.idxmax()
best_profit_category = category_profit.idxmax()
best_margin_category = category_summary["Profit_Margin"].idxmax()
best_sales_region = region_sales.idxmax()
best_profit_region = region_profit.idxmax()
best_profit_month = monthly_profit.idxmax()

print("\n" + "=" * 70)
print("BUSINESS INSIGHTS")
print("=" * 70)

print(
    f"1. Top-selling product: {best_sales_product} "
    f"with sales of {product_sales.max():,.0f}."
)

print(
    f"2. Most profitable product: {best_profit_product} "
    f"with profit of {product_profit.max():,.0f}."
)

print(
    f"3. Highest-selling category: {best_sales_category} "
    f"with sales of {category_sales.max():,.0f}."
)

print(
    f"4. Highest-profit category: {best_profit_category} "
    f"with profit of {category_profit.max():,.0f}."
)

print(
    f"5. Highest profit-margin category: {best_margin_category} "
    f"with a margin of {category_summary['Profit_Margin'].max():.2f}%."
)

print(
    f"6. Highest-sales region: {best_sales_region} "
    f"with sales of {region_sales.max():,.0f}."
)

print(
    f"7. Highest-profit region: {best_profit_region} "
    f"with profit of {region_profit.max():,.0f}."
)

print(
    f"8. Most profitable month: {best_profit_month} "
    f"with profit of {monthly_profit.max():,.0f}."
)

print(
    f"9. Overall profit margin: {profit_margin:.2f}%."
)


# ============================================================
# END
# ============================================================

print("\n" + "=" * 70)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)
