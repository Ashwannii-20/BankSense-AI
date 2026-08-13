# BankSense AI

## Banking Customer Risk Analysis & Machine Learning

BankSense AI is an end-to-end banking analytics and machine learning project designed to identify customers who may be at higher financial risk.

The project demonstrates a practical workflow covering data profiling, data cleaning, feature engineering, exploratory analysis, machine learning, model evaluation, and documentation.

> **Project status:** Completed initial ML modelling and model selection. The selected model is not production-ready and requires further improvement and validation.

---

## Business Problem

Banks and financial institutions need to identify customers who may represent higher credit or financial risk.

The objective of this project is to use customer-level financial and demographic information to predict a binary `high_risk` outcome.

The project focuses particularly on the challenge of **imbalanced classification**, where high-risk customers represent a small minority of the dataset.

---

## Project Objectives

- Profile and understand the customer dataset
- Identify and address data-quality issues
- Clean and prepare the data for analysis
- Engineer useful features
- Encode categorical variables
- Prepare the dataset for machine learning
- Compare Logistic Regression and Random Forest models
- Evaluate models using appropriate classification metrics
- Pay particular attention to minority-class detection
- Select the strongest candidate model based on F1 and ROC-AUC
- Document model limitations and areas for future improvement

---

## Dataset

The project uses a global banking customer dataset containing demographic, financial, employment, geographic, and customer-tenure information.

The final modelling dataset contains:

- **5,000 customers**
- **42 encoded predictor features**
- **Binary target:** `high_risk`
- **Training set:** 4,000 observations
- **Test set:** 1,000 observations

### Target Distribution

| Class | Customers | Proportion |
|---|---:|---:|
| Low Risk (0) | 4,654 | 93.08% |
| High Risk (1) | 346 | 6.92% |

The strong class imbalance makes accuracy alone an unsuitable measure of model performance.

---

## Methodology

The project follows this workflow:

```text
Data Profiling
      ↓
Problem Identification
      ↓
Data Cleaning
      ↓
Cleaning Validation
      ↓
Feature Engineering
      ↓
Exploratory Analysis
      ↓
Train/Test Split
      ↓
Model Development
      ↓
Model Evaluation
      ↓
Model Comparison
      ↓
Final Model Selection
      ↓
Post-Selection Validation