# 🛵 Zomato Delivery Operations: Exploratory Data Analysis (EDA)

## 📌 Executive Summary

This project performs an end-to-end Exploratory Data Analysis (EDA) on a real-world Zomato logistics dataset containing over 45,000 delivery records. The objective of this project is to uncover operational bottlenecks and mathematically quantify how factors like weather, traffic density, delivery distance, and driver demographics impact the Estimated Time of Arrival (ETA).

## 🎯 Key Insights

Through data cleaning, feature engineering (Haversine distance calculation), and statistical visualization, the following operational insights were discovered:

1. **Traffic is the Ultimate Bottleneck:** Deliveries in "Jam" traffic conditions take significantly longer (an average of +15 mins) compared to "Low" traffic conditions.
2. **Weather Causes ETA Variance:** Adverse weather conditions, specifically Fog and Sandstorms, cause the highest delay variance, indicating a need for dynamic "bad weather" ETA adjustments.
3. **The Physics of Delivery:** There is a direct positive correlation between geographic distance and delivery time. However, massive outliers exist where short distances (<5km) took >40 minutes, pointing to severe restaurant-side preparation delays.
4. **Fleet Optimization:** Pairing specific vehicle types (e.g., bicycles) with older age demographics across long distances yields the lowest operational efficiency.

## 📂 Project Structure

This project strictly follows professional Data Science directory standards:

```text
zomato-delivery-eda/
├── data/
│   ├── processed/         # Cleaned and engineered dataset
│   └── raw/               # Original Kaggle CSV
├── figures/               # 6 exported visualizations
├── notebooks/
│   └── 01-eda.ipynb       # Initial exploration, sandbox, and imputation testing
├── src/
│   ├── data_cleaning.py   # Python module for handling nulls & Haversine distance
│   └── visualisation.py   # Python module to generate standard charts
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 📊 Visualizations Included

The `figures/` directory contains the following exported charts. Here are the most impactful operational insights:

### 1. The Bottleneck: Traffic Density vs. Delivery Time

_Deliveries in "Jam" traffic take significantly longer, creating the largest operational bottleneck._
<img src="figures/02_traffic_impact.png" width="800">

### 2. The Physics: Distance vs. Delivery Time

_While distance correlates with time, the extreme outliers (high time, low distance) indicate restaurant-side preparation delays._
<img src="figures/05_distance_correlation.png" width="800">

### 3. Fleet Optimization: Vehicle Type & Driver Age

_This matrix highlights inefficiencies, such as older demographics using bicycles over long distances._
<img src="figures/06_vehicle_and_age_impact.png" width="800">

_(Note: Additional charts regarding Weather Impact, Baseline ETA Distribution, and Driver Ratings are available in the `figures/` folder)._

## 🚀 How to Run the Pipeline

### 1. Clone the Repository

```bash
git clone https://github.com/Debzillaa/zomato-delivery-eda.git
cd zomato-delivery-eda
```

### 2. Set Up the Environment

Create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add the Raw Data

Download the [Zomato Delivery Dataset from Kaggle](https://www.kaggle.com/datasets/saurabhbadole/zomato-delivery-operations-analytics-dataset) and place the CSV file inside the `data/raw/` folder. Name it `zomato-dataset.csv`.

### 4. Execute the Code

Run the data cleaning and feature engineering script:

```bash
python src/data_cleaning.py
```

Generate the visualisations:

```bash
python src/visualisation.py
```
