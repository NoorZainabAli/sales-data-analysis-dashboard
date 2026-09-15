# 📊 Sales Data Analysis Dashboard

A Python-based data analytics project that analyzes sales data using **Pandas**, **NumPy**, and **Matplotlib**. The project cleans raw sales data, performs business analysis, calculates profit, generates insightful visualizations, and exports processed reports.

---

## 📌 Project Overview

The **Sales Data Analysis Dashboard** is designed to demonstrate data analysis techniques using Python. It processes a sales dataset to uncover business insights such as monthly sales trends, product performance, regional sales, and profitability. The project also generates professional charts and exports the analyzed data into a CSV report.

---

## ✨ Features

* 📂 Import sales data from a CSV file
* 🧹 Clean the dataset by checking missing values and duplicates
* 📅 Monthly sales trend analysis
* 📦 Product-wise sales analysis
* 🛒 Category-wise sales analysis
* 🌍 Region-wise sales analysis
* 💰 Profit calculation and analysis
* 🏆 Identify top and bottom performing products
* 📊 Generate bar charts, line charts, pie charts, and histograms
* 💾 Export processed data to a CSV report
* 🌐 Version control using Git and GitHub

---

## 🛠️ Technologies Used

* **Python 3**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Git**
* **GitHub**

---

## 📂 Project Structure

```text
Sales-Data-Analysis-Dashboard/
│
├── analysis.py
├── sales_data.csv
├── sales_report.csv
├── monthly_sales.png
├── product_sales.png
├── category_sales.png
├── region_sales.png
├── profit_distribution.png
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

The dataset contains the following columns:

| Column   | Description             |
| -------- | ----------------------- |
| Order_ID | Unique order identifier |
| Date     | Order date              |
| Region   | Sales region            |
| Category | Product category        |
| Product  | Product name            |
| Sales    | Sales amount            |
| Quantity | Quantity sold           |
| Cost     | Cost of the product     |

---

## 📈 Analysis Performed

The project performs the following analyses:

* Dataset inspection (`head()`, `tail()`, `shape`, `info()`, `describe()`)
* Missing value detection
* Duplicate detection and removal
* Monthly sales trend analysis
* Product-wise sales analysis
* Category-wise sales analysis
* Region-wise sales analysis
* Profit calculation
* Top & bottom performing products
* Sales report generation

---

## 📊 Visualizations

The project generates the following charts:

* 📈 Monthly Sales Trend (Line Chart)
* 📊 Product-wise Sales (Bar Chart)
* 🥧 Category-wise Sales (Pie Chart)
* 📊 Region-wise Sales (Bar Chart)
* 📉 Profit Distribution (Histogram)

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SmrutiSurekhaPati-hub/Sales-Data-Analysis-Dashboard.git
```

### 2️⃣ Navigate to the project folder

```bash
cd Sales-Data-Analysis-Dashboard
```

### 3️⃣ Install required libraries

```bash
pip install pandas numpy matplotlib
```

### 4️⃣ Run the project

```bash
python analysis.py
```

---

## 📁 Output

After execution, the project generates:

* `sales_report.csv`
* `monthly_sales.png`
* `product_sales.png`
* `category_sales.png`
* `region_sales.png`
* `profit_distribution.png`

---

## 🎯 Learning Outcomes

This project demonstrates practical skills in:

* Data cleaning using Pandas
* Working with CSV datasets
* Data aggregation using `groupby()`
* Profit analysis
* Business data visualization
* Statistical analysis
* Python programming
* Git and GitHub version control

---
### 📈 Monthly Sales Trend

![Monthly Sales](visualizations/monthly_sales.png)

---

### 📊 Product-wise Sales

![Product Sales](visualizations/product_sales.png)

---

### 🥧 Category-wise Sales

![Category Sales](visualizations/category_sales.png)

---

### 🌍 Region-wise Sales

![Region Sales](visualizations/region_sales.png)

---

### 💰 Profit Distribution

![Profit Distribution](visualizations/profit_distribution.png)

## 👩‍💻 Author

**Noor Zainab Ali**

**GitHub Profile:**
[https://github.com/SmrutiSurekhaPati-hub](https://github.com/NoorZainabAli)


---

## 🔮 Future Enhancements

* Interactive dashboard using **Streamlit**
* Power BI dashboard integration
* Excel and PDF report export
* SQL database connectivity
* Sales forecasting using Machine Learning
* Interactive filters and KPI dashboard

---

## 🤝 Contributions

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is created for **learning, educational, and portfolio purposes**.
