# BankSense AI

## Banking Customer Risk Analysis & Machine Learning

BankSense AI is an end-to-end banking analytics and machine learning project designed to identify customers who may be at higher financial risk.

The project demonstrates a practical workflow covering data profiling, data cleaning, feature engineering, exploratory analysis, machine learning, model evaluation, model selection, model persistence, prediction, and an interactive Streamlit application.

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
- Save the selected model for future predictions
- Build a reusable prediction pipeline
- Develop an interactive Streamlit application
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
      ↓
Model Persistence
      ↓
Prediction Pipeline
      ↓
Streamlit Application
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

## Model Persistence & Prediction

The selected Tuned Random Forest model was saved as a reusable Joblib artifact:

```text
models/banksense_rf_tuned.joblib
```

The saved artifact contains the trained model and the feature-column structure required for prediction.

The project also includes reusable preprocessing and prediction modules:

- `src/banksense_ai/preprocessing.py`
- `src/banksense_ai/predict.py`

The prediction pipeline:

1. Accepts customer information
2. Creates the required tenure groups
3. Applies categorical encoding
4. Aligns the prediction features with the 42 training features
5. Loads the saved Random Forest model
6. Generates a high-risk classification
7. Generates a high-risk probability

---

## Streamlit Application

BankSense AI includes an interactive Streamlit application that allows users to enter customer information and obtain a model-based risk assessment.

The application accepts:

- Age
- Annual income
- Customer tenure
- Gender
- Country
- Occupation
- Employment status

The application returns:

- High-risk or low-risk prediction
- High-risk probability

Example:

```text
Prediction: Low Risk
High-Risk Probability: 49.47%
```

> **Important:** The prediction is a machine-learning estimate and should not be treated as a definitive financial or credit decision.

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
- The Tuned Random Forest achieved the strongest F1 Score and ROC-AUC among the evaluated models.
- The model was successfully saved as a reusable Joblib artifact.
- A reusable preprocessing and prediction pipeline was developed.
- A Streamlit application was developed to provide an interactive interface for model predictions.
- The results indicate that further modelling improvements are required before practical deployment.

---

## Limitations

The current model has several limitations:

- Limited predictive performance based on the current F1 and ROC-AUC results.
- Strong class imbalance between low-risk and high-risk customers.
- The current feature set may not contain sufficient information to reliably distinguish high-risk customers.
- Further validation is required before the model could be considered suitable for real-world banking decisions.
- The project should not be interpreted as a production credit-risk system.
- The Streamlit application is currently intended for local demonstration and has not been deployed as a production service.

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
- Deployment and hosting of the Streamlit application

---

## Technology Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Joblib**
- **Streamlit**
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
├── models/
│   └── banksense_rf_tuned.joblib
│
├── notebooks/
│   └── 01_banksense_risk_analysis.ipynb
│
├── src/
│   └── banksense_ai/
│       ├── __init__.py
│       ├── predict.py
│       └── preprocessing.py
│
├── app.py
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── uv.lock
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Ashwannii-20/BankSense-AI.git
cd BankSense-AI
```

### 2. Install Dependencies

The project uses `uv` for environment and dependency management.

```bash
uv sync
```

### 3. Run the Jupyter Notebook

Launch Jupyter:

```bash
uv run jupyter notebook
```

Then open:

```text
notebooks/01_banksense_risk_analysis.ipynb
```

### 4. Launch the BankSense AI Application

Start the Streamlit application:

```bash
uv run streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

---

## Project Scope

BankSense AI is an educational and portfolio project demonstrating an end-to-end machine learning workflow in a banking-risk context.

The project demonstrates:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Exploratory Analysis
   ↓
Model Development
   ↓
Model Evaluation
   ↓
Model Selection
   ↓
Model Persistence
   ↓
Prediction Pipeline
   ↓
Interactive Application
```

The current model is a candidate model for demonstration purposes and requires additional modelling, validation, and deployment work before it could be considered for real-world financial decision-making.