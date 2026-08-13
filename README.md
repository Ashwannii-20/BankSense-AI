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
```

---

## Model Development & Evaluation

Two classification approaches were evaluated:

- Logistic Regression
- Random Forest

Because the target variable is highly imbalanced, model performance was assessed using metrics beyond accuracy, with particular attention to minority-class detection.

The evaluation focused on:

- Precision
- Recall
- F1 Score
- ROC-AUC

---

## Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Baseline Logistic Regression with Engineered Features | 0.5590 | 0.0792 | 0.5072 | 0.1370 | 0.5601 |
| Improved Logistic Regression | 0.5560 | 0.0787 | 0.5072 | 0.1362 | 0.5600 |
| Baseline Random Forest | 0.9260 | 0.0000 | 0.0000 | 0.0000 | 0.5423 |
| Tuned Random Forest | 0.7290 | 0.1055 | 0.3913 | 0.1662 | 0.5710 |

The baseline Random Forest achieved high accuracy but failed to identify any high-risk customers, resulting in zero recall and zero F1 score.

The tuned Random Forest improved minority-class detection and achieved the highest F1 score and ROC-AUC among the evaluated models.

---

## Final Model Selection

The **Tuned Random Forest** was selected as the strongest candidate among the evaluated models because it achieved:

- **F1 Score:** 0.1662
- **ROC-AUC:** 0.5710

The model improved high-risk customer detection compared with the baseline Random Forest.

However, its relatively low precision and ROC-AUC indicate that overall predictive performance remains limited. Therefore, the model should **not be considered production-ready** without further improvement and validation.

Because the target variable is highly imbalanced, accuracy was not used as the primary criterion for model selection.

---

## Key Findings

- The dataset contains a significant class imbalance, with high-risk customers representing **6.92%** of observations.
- Accuracy alone can therefore provide a misleading assessment of model performance.
- The credit-score-based target mapping was validated successfully.
- The final feature matrix contains **42 predictor variables**.
- The training and test datasets contain **4,000 and 1,000 observations**, respectively.
- The training and test sets contain the same feature structure.
- Train/test index validation confirmed **no overlapping observations**.
- Post-selection validation confirmed that the final feature matrix contains **no missing values**.
- The results indicate that further modelling improvements are required before practical deployment.

---

## Limitations

The current model has several limitations:

- Limited predictive performance based on the current F1 and ROC-AUC results.
- Strong class imbalance between low-risk and high-risk customers.
- The current feature set may not contain sufficient information to reliably distinguish high-risk customers.
- Further validation is required before the model could be considered suitable for real-world banking decisions.
- The project should not be interpreted as a production credit-risk system.

---

## Future Improvements

Potential next steps include:

- Additional feature engineering
- More detailed analysis of minority-class behaviour
- Further hyperparameter optimization
- Probability-threshold optimization
- Additional imbalance-handling techniques
- Evaluation of additional classification algorithms
- Cross-validation and robustness testing
- Feature importance and model interpretability analysis
- Probability calibration
- Evaluation on an independent external dataset

---

## Technology Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Jupyter Notebook**
- **uv**
- **Git & GitHub**

---

## Project Structure

```text
BankSense-AI/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   └── 01_banksense_risk_analysis.ipynb
│
├── src/
│   └── banksense_ai/
│       └── __init__.py
│
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── uv.lock
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Ashwannii-20/BankSense-AI.git
cd BankSense-AI
```

Install the project environment and dependencies using `uv`:

```bash
uv sync
```

Launch Jupyter:

```bash
uv run jupyter notebook
```

Then open:

```text
notebooks/01_banksense_risk_analysis.ipynb
```

> **Note:** The project dataset is not included in the public repository. The `.gitignore` configuration excludes CSV data files from version control.

---

## Project Status

**Completed:** Initial data profiling, data cleaning, feature engineering, exploratory analysis, model development, model evaluation, model comparison, final model selection, and post-selection validation.

**Current status:** The Tuned Random Forest is the strongest candidate among the evaluated models but is **not production-ready** due to limited predictive performance.

**Next stage:** Improve predictive performance, validate robustness, and develop a deployable application.
