Clinical Readmission Prediction & Clinical Decision Support

An interpretable machine learning pipeline for predicting 30-day hospital readmission risk and translating predictive outputs into risk-stratified, clinically interpretable decision-support recommendations.

---

Overview

Hospital readmission within 30 days is an important indicator of healthcare quality, continuity of care, and patient safety. Early identification of patients at elevated risk of readmission can support targeted follow-up, discharge planning, and allocation of post-discharge care resources.

This project develops a reproducible machine learning workflow for predicting 30-day hospital readmission using structured clinical data. In addition to predictive modeling, the project demonstrates how machine learning outputs can be transformed into a more clinically meaningful decision-support layer.

The workflow integrates:

- Data preprocessing and preparation
- Interpretable predictive modeling
- Comparative machine learning evaluation
- Risk stratification
- Model performance assessment
- Feature importance analysis
- Confidence-aware interpretation of predictions
- Fairness-oriented model assessment
- Cost-sensitive clinical recommendations
- Human-readable clinical decision-support outputs

The project is designed as a research and educational demonstration of the transition from predictive analytics to clinically interpretable decision support.

---

Clinical Problem

Hospital readmissions are influenced by multiple clinical and healthcare-related factors. A predictive model can help identify patients who may require additional attention after discharge.

However, prediction alone is not sufficient for clinical decision-making.

A clinically useful system should also help answer:

«What does the predicted risk mean, and what type of additional action may be appropriate?»

This project therefore extends beyond a conventional binary prediction task by incorporating a decision-support layer that translates model outputs into interpretable risk categories and potential care recommendations.

---

Project Workflow

Structured Clinical Data
          │
          ▼
   Data Preprocessing
          │
          ▼
  Feature Preparation
          │
          ▼
 ┌─────────────────────┐
 │ Predictive Modeling │
 └─────────────────────┘
          │
     ┌────┴────┐
     ▼         ▼
Logistic    Random
Regression  Forest
     │         │
     └────┬────┘
          ▼
 Model Evaluation
          │
          ▼
  Feature Importance
          │
          ▼
   Risk Stratification
          │
          ▼
 Clinical Decision Support
          │
          ▼
 Human-Readable Recommendations

---

Predictive Modeling

Two complementary machine learning approaches are implemented:

Logistic Regression

Logistic Regression provides an interpretable baseline model for estimating the probability of 30-day readmission.

Its advantages include:

- Transparent model structure
- Interpretable feature coefficients
- Probability-based risk estimation
- Suitability for clinical research and explainable prediction

Random Forest

Random Forest is used as a non-linear comparative model capable of capturing more complex relationships between clinical features and readmission risk.

The comparison between Logistic Regression and Random Forest provides insight into the trade-off between:

- Interpretability
- Predictive performance
- Model complexity
- Non-linear pattern recognition

---

Clinical Decision-Support Layer

The project extends the prediction pipeline with a decision-support component designed to make model outputs more clinically interpretable.

The system includes:

Risk Stratification

Patients are categorized into different risk levels based on predicted readmission probability.

This supports prioritization of patients who may benefit from:

- Additional discharge planning
- Enhanced follow-up
- Medication review
- Care coordination
- Post-discharge monitoring

Confidence-Aware Interpretation

The system considers the uncertainty associated with model predictions and provides a more cautious interpretation of borderline or uncertain predictions.

This is important because clinical decisions should not rely solely on a probability score without considering the reliability and context of the prediction.

Fairness-Oriented Assessment

The project includes a fairness-oriented evaluation component to encourage examination of whether model performance may vary across patient subgroups.

This reflects an important principle in healthcare AI:

«Predictive performance should be evaluated not only globally, but also across relevant patient populations.»

Cost-Sensitive Recommendations

The decision-support layer considers the potential consequences of different types of prediction errors.

For example:

- Missing a high-risk patient may delay appropriate follow-up.
- Over-classifying a low-risk patient may lead to unnecessary resource utilization.

The system therefore demonstrates how predictive outputs can be connected to more context-aware recommendations rather than treated as isolated classifications.

---

Evaluation

Model performance is evaluated using multiple complementary metrics:

- AUC-ROC – Overall discrimination between patients with and without readmission
- Precision – Proportion of predicted high-risk patients who were actually readmitted
- Recall – Ability to identify patients who experienced readmission
- F1-score – Balance between precision and recall

Using multiple evaluation metrics is particularly important in healthcare prediction, where the consequences of false-negative and false-positive predictions may differ.

---

Feature Importance and Interpretability

The project includes feature importance analysis to examine which input variables contribute most strongly to model predictions.

Interpretability is emphasized because clinical machine learning systems should support understanding rather than function exclusively as black-box predictors.

The analysis is intended to help answer:

- Which clinical features are most influential?
- How do different models rank important features?
- Can model outputs be communicated in a clinically understandable manner?

---

Repository Structure

clinical-readmission-prediction/
│
├── train_model.py
│   └── Model training and predictive pipeline
│
├── Clinical_decision-support.py
│   └── Risk stratification and clinical decision-support logic
│
├── .ipynb
│   └── Interactive exploratory analysis and experimentation
│
├── Requirements.txt
│   └── Python dependencies
│
├── .gitignore
│   └── Files excluded from version control
│
└── README.md
    └── Project documentation

---

Technologies

- Python
- pandas
- scikit-learn
- NumPy
- Matplotlib
- Jupyter Notebook

---

Installation

1. Clone the repository

git clone https://github.com/SharareTaheriMoghadam/clinical-readmission-prediction.git
cd clinical-readmission-prediction

2. Install dependencies

pip install -r Requirements.txt

3. Run the predictive modeling pipeline

python train_model.py

4. Run the clinical decision-support component

python "Clinical_decision-support.py"

---

Research and Educational Scope

This repository is intended for:

- Research and educational purposes
- Demonstration of healthcare machine learning workflows
- Exploration of interpretable clinical prediction
- Development of clinical decision-support concepts
- Experimentation with risk stratification and model evaluation

The project uses sample or demonstration data and is not intended to replace clinical judgment or provide autonomous medical diagnosis or treatment recommendations.

---

Key Concept

The central objective of this project is to demonstrate a transition from:

Machine Learning Prediction
          ↓
Risk Estimation
          ↓
Interpretation
          ↓
Risk Stratification
          ↓
Clinical Decision Support

The project therefore represents an early-stage example of how predictive machine learning can be integrated with interpretable decision-support logic to support more clinically meaningful healthcare AI systems.

---

Future Development

Potential future extensions include:

- External validation using independent datasets
- Calibration analysis
- SHAP-based explainability
- Temporal clinical data modeling
- Advanced imbalance-handling strategies
- Subgroup-specific performance evaluation
- Clinical knowledge integration
- Ontology-based patient risk representation
- Integration with clinical knowledge graphs
- Prospective clinical validation

---

Author

Sharare Taheri Moghadam, PhD

Medical Informatics | Healthcare AI | Clinical Decision Support | Patient Safety | Biomedical Knowledge Representation

---

Disclaimer

This project is intended for research, educational, and demonstration purposes only. It does not constitute medical advice and should not be used as an autonomous clinical decision-making system.
