
Ontology-Enhanced Explainable Clinical Readmission Prediction

An Interpretable Machine Learning Framework for Risk Stratification and Human–AI Clinical Decision Support

"Python" --->
"Machine Learning" --->
"Explainable AI" --->
"Ontology" --->
"Healthcare AI" --->
"Status"

---

Overview

Hospital readmission within 30 days is an important indicator of healthcare quality, continuity of care, resource utilization, and patient safety. Early identification of patients at elevated risk can support targeted discharge planning, follow-up, medication review, and allocation of post-discharge resources.

This project develops a reproducible and interpretable machine learning framework for 30-day clinical readmission prediction and extends conventional predictive modeling with an Explainable AI and ontology-enhanced clinical decision-support layer.

The framework is designed to demonstrate how a predictive model can evolve from simply estimating readmission probability toward producing a more transparent and clinically contextualized Human–AI decision-support artifact.

The overall pipeline integrates:

- Clinical data preprocessing
- Feature engineering and preparation
- Interpretable machine learning
- Comparative model evaluation
- Risk probability estimation
- Risk stratification
- Feature importance analysis
- SHAP-based explainability
- LIME-based local explanation
- Confidence-aware interpretation
- Fairness-oriented assessment
- Cost-sensitive decision-support logic
- Clinical knowledge representation
- MSCDO-based semantic contextualization
- Ontology mapping
- Human-readable clinical recommendations

«Core principle: A prediction is not, by itself, a clinical decision.»

The purpose of this project is therefore not only to predict who may be at higher risk, but also to explore how the prediction can be explained, contextualized, semantically represented, and presented as decision support while preserving clinician authority.

---

Research Motivation

Traditional clinical prediction systems commonly follow a relatively simple workflow:

Clinical Data
     ↓
Machine Learning Model
     ↓
Risk Prediction

Although such systems can achieve useful predictive performance, a probability score alone does not adequately answer the questions that matter to clinical users:

- Why is this patient considered high risk?
- Which clinical factors contributed to the prediction?
- How confident should we be in the prediction?
- What patient-safety context may be associated with those factors?
- What type of follow-up or review may be appropriate?
- How can clinical knowledge be connected to the prediction?
- How can clinicians retain control over the final decision?

This project explores an extended architecture:

Clinical Data
     ↓
Machine Learning Prediction
     ↓
Explainability
     ↓
Risk Stratification
     ↓
Clinical Knowledge Representation
     ↓
Ontology-Based Contextualization
     ↓
Decision-Support Artifact
     ↓
Human–AI Clinical Decision Support

The central research objective is therefore:

«To explore how interpretable machine learning can be combined with explainability and biomedical knowledge representation to transform clinical risk prediction into transparent, knowledge-grounded decision support.»

---

Clinical Problem

Hospital readmission is influenced by multiple interacting factors, including:

- Previous hospitalization
- Comorbidities
- Medication burden
- Clinical conditions
- Laboratory abnormalities
- Demographic and contextual characteristics
- Healthcare utilization patterns
- Discharge and follow-up factors

A predictive model can identify statistical patterns associated with readmission. However, predictive performance alone does not establish clinical usefulness.

A clinically meaningful AI system should provide a pathway from:

Risk → Explanation → Clinical Context → Potential Action

This project therefore treats readmission prediction as the first component of a broader clinical decision-support pipeline rather than as an isolated binary classification problem.

---

Framework Architecture

                    STRUCTURED CLINICAL DATA
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Data Preprocessing  │
                    │ & Feature Preparation│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Predictive Modeling │
                    │                     │
                    │ Logistic Regression │
                    │ Random Forest       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Readmission Risk   │
                    │   Probability       │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
          SHAP / LIME    Feature Analysis   Confidence
                │              │              │
                └──────────────┼──────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Risk Stratification │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Knowledge & Semantic │
                    │ Representation Layer │
                    │                     │
                    │ MSCDO / OWL / RDF   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Clinical Contextual │
                    │ Interpretation      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Decision-Support    │
                    │ Artifact            │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Human–AI Co-Decision│
                    │ Support             │
                    └─────────────────────┘

---

1. Machine Learning Prediction Layer

The core predictive pipeline uses supervised machine learning to estimate the probability of 30-day hospital readmission.

Two complementary models are included.

Logistic Regression

Logistic Regression provides an interpretable statistical baseline for binary readmission prediction.

Key advantages include:

- Transparent model structure
- Interpretable coefficients
- Probability-based risk estimation
- Strong baseline for clinical prediction research
- Relatively straightforward interpretation

Random Forest

Random Forest provides a non-linear comparative model capable of representing more complex relationships between clinical variables.

It provides an opportunity to examine the trade-off between:

- Predictive performance
- Interpretability
- Model complexity
- Non-linear pattern recognition

Comparing these models provides a useful foundation for understanding how model choice affects both prediction and interpretation.

---

2. Risk Stratification

Predicted probabilities are transformed into clinically interpretable risk categories.

For example:

Predicted Probability
        ↓
Risk Stratification
        ↓
Low / Moderate / High Risk

Risk stratification is intended to support prioritization of patients who may potentially benefit from additional attention, such as:

- Enhanced discharge planning
- Medication review
- Care coordination
- Post-discharge follow-up
- Additional monitoring
- Clinical reassessment

The risk category is treated as a decision-support signal, not as an autonomous clinical decision.

---

3. Explainable AI Layer

The framework extends conventional feature importance analysis with post-hoc explainability methods.

SHAP

SHAP (SHapley Additive exPlanations) is used to investigate the contribution of individual features to model predictions.

SHAP can support both:

Global interpretation

Understanding which variables are influential across the population.

Local interpretation

Understanding which variables contribute to an individual patient's predicted risk.

Conceptually:

Patient Prediction
       │
       ▼
Readmission Risk = 0.82
       │
       ▼
 ┌───────────────┐
 │ SHAP Analysis │
 └───────┬───────┘
         │
         ├── Previous hospitalization
         ├── Medication burden
         ├── Comorbidity profile
         └── Clinical measurements

This allows the system to move from:

«"The patient is high risk."»

toward:

«"The model estimates high risk, and these factors contributed substantially to the prediction."»

---

LIME

LIME (Local Interpretable Model-Agnostic Explanations) provides another approach for explaining individual predictions by approximating model behavior locally.

LIME is particularly useful for:

- Patient-level explanations
- Model-agnostic interpretation
- Comparing explanations across different models
- Human-centered exploration of model outputs

SHAP and LIME are therefore treated as complementary explainability approaches rather than as replacements for clinical reasoning.

---

4. Confidence-Aware Interpretation

Clinical prediction systems should avoid presenting every probability as equally reliable.

The framework therefore includes a confidence-aware interpretation concept in which predictions near decision boundaries or otherwise uncertain cases can be treated more cautiously.

Conceptually:

Prediction
    │
    ├── Clear high-risk signal
    │        ↓
    │   Stronger prioritization
    │
    ├── Clear low-risk signal
    │        ↓
    │   Lower prioritization
    │
    └── Borderline / uncertain
             ↓
      Additional clinical review

This reflects an important principle for healthcare AI:

«Uncertainty should inform human oversight rather than be hidden behind a binary prediction.»

---

5. Fairness-Oriented Assessment

Healthcare AI systems should not be evaluated solely using aggregate performance metrics.

The project therefore incorporates a fairness-oriented evaluation perspective to encourage examination of whether predictive performance differs across relevant patient subgroups.

Potential subgroup analyses include comparisons of:

- Discrimination
- Precision
- Recall
- F1-score
- False-positive rates
- False-negative rates

The objective is not to claim that the model is automatically fair, but to provide a framework for examining potential performance disparities.

---

6. Cost-Sensitive Clinical Decision Support

Different prediction errors can have different consequences in healthcare.

For example:

False negative

High-risk patient
       ↓
Predicted as low risk
       ↓
Potentially missed follow-up opportunity

False positive

Low-risk patient
       ↓
Predicted as high risk
       ↓
Potentially unnecessary resource utilization

The decision-support layer therefore considers the clinical implications of different prediction errors rather than treating all classification errors as equivalent.

This provides a conceptual bridge between machine learning performance and clinical decision-making.

---

7. Ontology-Enhanced Clinical Knowledge Representation

A major extension of this project is the incorporation of biomedical knowledge representation.

The framework explores the use of the:

Medication Safety Co-Decision Ontology (MSCDO)

MSCDO provides a semantic framework for representing concepts related to medication safety and human–AI collaborative decision support.

Within this project, ontology integration is intended to provide a bridge between:

Machine Learning Features
          ↓
Prediction & Explanation
          ↓
Clinical Concepts
          ↓
Patient Safety Context
          ↓
Decision-Support Concepts

This allows predictive features to be connected to structured clinical knowledge rather than being treated solely as numerical variables.

---

8. Feature-to-Ontology Mapping

The framework explores mapping selected clinical prediction features to semantically meaningful concepts.

Illustrative examples include:

Clinical / ML Feature| Semantic Representation
Medication count| Polypharmacy context
Drug interaction history| Drug–drug interaction
Medication-related adverse event| Adverse drug event
Patient characteristics| Patient context
Clinical diagnosis| Clinical condition
Predicted readmission probability| Risk profile
Risk category| Risk stratification
Clinical recommendation| Decision artifact

These mappings are intended as a semantic bridge between predictive analytics and knowledge-based decision support.

Important: the mapping layer should be interpreted according to the concepts and mappings actually implemented in the repository; illustrative mappings are not presented as claims of complete ontology coverage.

---

9. RDF-Based Clinical Risk Representation

The extended architecture supports representation of selected clinical risk information using semantic technologies such as:

- RDF
- OWL
- SPARQL
- Protégé

Conceptually, a prediction can be represented as a structured semantic object:

Patient
   │
   ├── hasClinicalCondition
   ├── hasMedicationContext
   ├── hasRiskProfile
   ├── hasRiskFactor
   └── hasDecisionArtifact

This provides a foundation for interoperability between machine learning outputs and structured biomedical knowledge.

---

10. Ontology-Enhanced Interpretation

The purpose of the ontology layer is not to replace the predictive model.

Instead, it provides semantic contextualization.

For example:

Machine Learning Output
        │
        ▼
Readmission probability = 0.78
        │
        ▼
High-risk category
        │
        ▼
Explainability
        │
        ├── Medication burden
        ├── Previous hospitalization
        └── Clinical comorbidity
        │
        ▼
Ontology-based contextualization
        │
        ├── Medication safety context
        ├── Patient safety concepts
        └── Relevant clinical relationships
        │
        ▼
Decision-support artifact

The resulting artifact can present:

- Predicted risk
- Risk category
- Contributing factors
- Relevant clinical context
- Potential areas for clinical review

---

11. Example Clinical Scenario

Consider a hypothetical patient with:

- Multiple medications
- Previous hospitalization
- Chronic disease history
- Renal impairment

The predictive model estimates:

Readmission probability = 0.78
Risk category = High

Explainability analysis identifies major contributing factors such as:

1. Previous hospitalization
2. Medication burden
3. Comorbidity profile
4. Renal impairment

The semantic layer can then contextualize relevant medication-safety concepts.

For example:

Renal impairment
       +
Medication exposure
       +
Potential medication-related risk
       ↓
Medication safety context
       ↓
Clinical review recommended

Potential decision-support outputs may include:

- Medication review
- Follow-up planning
- Care coordination
- Additional clinical assessment

These outputs are supportive recommendations for clinician consideration, not autonomous treatment decisions.

---

12. Human–AI Co-Decision Support

A central design principle of the framework is preservation of human clinical authority.

The system is therefore conceptualized as:

                 AI SYSTEM
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     Risk        Explanation   Clinical
   Prediction                   Context
        │           │           │
        └───────────┼───────────┘
                    ▼
          Decision-Support Artifact
                    │
                    ▼
               CLINICIAN
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      Accept / Use         Override /
      as appropriate       Reassess

The AI system provides evidence and structured decision support.

The clinician retains responsibility for interpreting the information within the patient's broader clinical context.

This human-in-the-loop design is particularly important for high-stakes healthcare applications.

---

13. Evaluation

Model performance is evaluated using multiple complementary metrics.

AUC-ROC

Measures the model's ability to discriminate between patients with and without readmission.

Precision

Measures the proportion of patients predicted as high risk who actually experienced readmission.

Recall

Measures the ability to identify patients who experienced readmission.

F1-score

Provides a balance between precision and recall.

Where appropriate, future evaluation can additionally include:

- Calibration
- Brier score
- Precision–recall curves
- Confusion matrices
- Subgroup performance
- Decision-curve analysis
- External validation

Multiple metrics are important because healthcare prediction involves asymmetric consequences for different types of errors.

---

14. Feature Importance and Interpretability

Interpretability is considered at multiple levels:

Model Level
     ↓
Which variables are generally important?

Patient Level
     ↓
Why was this patient classified as high risk?

Clinical Knowledge Level
     ↓
How can these factors be contextualized using structured knowledge?

Decision-Support Level
     ↓
What information should be presented to the clinician?

The framework therefore combines:

- Model-based feature importance
- SHAP
- LIME
- Risk stratification
- Semantic representation
- Ontology-based contextualization

This multi-level approach is intended to improve transparency rather than relying on a single explanation technique.

---

Repository Structure

clinical-readmission-prediction/
│
├── data/
│   └── README.md
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_model_training.ipynb
│   ├── 03_SHAP_explainability.ipynb
│   ├── 04_LIME_explainability.ipynb
│   └── 05_MSCDO_integration.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── models.py
│   ├── explainability.py
│   ├── risk_stratification.py
│   ├── clinical_decision_support.py
│   └── ontology_mapping.py
│
├── ontology/
│   └── MSCDO.owl
│
├── results/
│   └── README.md
│
├── train_model.py
├── Clinical_decision-support.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md

The exact repository structure may evolve as additional components are implemented.

---

Technologies

Programming

- Python
- pandas
- NumPy

Machine Learning

- scikit-learn
- Logistic Regression
- Random Forest

Explainable AI

- SHAP
- LIME

Visualization

- Matplotlib

Semantic Technologies

- OWL
- RDF
- SPARQL
- Protégé

Biomedical Knowledge Representation

- MSCDO
- SNOMED CT
- RxNorm
- LOINC
- UMLS
- WHO ICPS

Biomedical standards are considered as potential interoperability and knowledge-integration resources; their inclusion does not imply that every standard is currently implemented in the pipeline.

---

Installation

Clone the repository:

git clone https://github.com/SharareTaheriMoghadam/clinical-readmission-prediction.git
cd clinical-readmission-prediction

Install dependencies:

pip install -r requirements.txt

Run the predictive modeling pipeline:

python train_model.py

Run the clinical decision-support component:

python "Clinical_decision-support.py"

For notebook-based experimentation, run the notebooks sequentially according to their numbering.

---

Reproducible Research Workflow

The recommended workflow is:

01. Data Preprocessing
        ↓
02. Model Training
        ↓
03. Model Evaluation
        ↓
04. SHAP / LIME Explainability
        ↓
05. Risk Stratification
        ↓
06. Clinical Contextualization
        ↓
07. MSCDO / Ontology Integration
        ↓
08. Decision-Support Generation

This structure separates predictive modeling from interpretation and knowledge integration, making the framework easier to reproduce and extend.

---

Current Status

Completed / Established

- Clinical readmission prediction workflow
- Structured clinical data preprocessing
- Logistic Regression baseline
- Random Forest comparative modeling
- Model evaluation framework
- Risk stratification concept
- Feature importance analysis
- Clinical decision-support logic
- Explainable AI architecture
- MSCDO integration design

Extension / Development

- Automated SHAP explanation pipeline
- Automated LIME explanation pipeline
- Feature-to-ontology mapping
- RDF-based patient-risk representation
- Automated semantic reasoning
- Ontology-grounded recommendation generation
- Human-centered evaluation
- Subgroup/fairness evaluation
- Calibration analysis
- External validation

The repository distinguishes between implemented components and research extensions to maintain transparency and reproducibility.

---

Scientific Contribution

The main contribution of this repository is the demonstration of a conceptual and technical transition from conventional predictive analytics toward explainable, knowledge-enhanced clinical decision support.

Conventional approach

Clinical Data
     ↓
Prediction

Extended approach

Clinical Data
     ↓
Prediction
     ↓
Risk Estimation
     ↓
Explainability
     ↓
Risk Stratification
     ↓
Clinical Knowledge Representation
     ↓
Ontology-Based Contextualization
     ↓
Decision-Support Artifact
     ↓
Human–AI Co-Decision Support

This architecture reflects a broader research direction in trustworthy healthcare AI: predictive models should not only be accurate, but also interpretable, context-aware, knowledge-grounded, and designed to support appropriate human oversight.

---

Relation to TrustMedAI

This repository represents a foundational component of the broader TrustMedAI research direction.

The conceptual connection is:

Clinical Prediction
       │
       ▼
Explainable AI
       │
       ▼
Biomedical Ontologies
       │
       ▼
Knowledge Graphs
       │
       ▼
Clinical Decision Support
       │
       ▼
Trustworthy Human–AI Collaboration

The project therefore provides a practical bridge between:

- Machine learning
- Explainable AI
- Clinical decision support
- Biomedical knowledge representation
- Patient safety
- Human–AI collaboration

Future integration with knowledge graphs and ontology-driven reasoning can further extend this architecture toward more comprehensive trustworthy clinical AI systems.

---

Future Development

Future versions may investigate:

1. External Validation

Validation using independent clinical datasets and, where feasible, multi-center cohorts.

2. Calibration

Assessment of whether predicted probabilities correspond appropriately to observed readmission frequencies.

3. Advanced Explainability

Integration of SHAP, LIME, counterfactual explanations, and other human-centered explanation approaches.

4. Temporal Clinical Modeling

Incorporation of longitudinal EHR information rather than relying exclusively on static patient features.

5. Knowledge Graph Integration

Transformation of patient-level clinical information into graph-based representations.

6. Ontology-Based Reasoning

Development of automated semantic reasoning mechanisms connecting predicted risk factors with clinical knowledge.

7. Clinical Recommendation Generation

Generation of ontology-grounded decision-support artifacts while maintaining clinician oversight.

8. Fairness and Subgroup Evaluation

Systematic evaluation of performance across clinically relevant patient populations.

9. Human-Centered Evaluation

Assessment of how clinicians understand, trust, interact with, and act upon AI-generated explanations and recommendations.

10. Federated / Multi-Center Learning

Investigation of privacy-preserving approaches for multi-institutional validation.

---

Research Positioning

The project can be viewed as an evolving research prototype at the intersection of:

Clinical Machine Learning + Explainable AI + Biomedical Ontologies + Patient Safety + Human–AI Decision Support

Rather than positioning the system as a deployed clinical product, this repository provides a reproducible research environment for investigating how these components can be combined.

---

Research and Educational Scope

This repository is intended for:

- Research
- Education
- Healthcare AI experimentation
- Explainable machine learning research
- Clinical decision-support research
- Biomedical knowledge representation
- Ontology integration
- Human–AI collaboration research

The project is particularly suitable for demonstrating the progression from a conventional machine learning model to an interpretable and knowledge-enhanced clinical AI architecture.

---

Citation

If you use or build upon this repository, please cite the associated research work:

«Clinical Readmission Prediction with Explainable AI and Ontology-Enhanced Human–AI Decision Support.»

A formal citation will be added when the associated manuscript is published.

---

Author

Sharare Taheri Moghadam, PhD

Medical Informatics | Healthcare AI | Clinical Decision Support | Patient Safety | Explainable AI | Biomedical Knowledge Representation

---

Disclaimer

This repository is intended for research, educational, and demonstration purposes only.

It does not constitute medical advice and is not intended to provide autonomous diagnosis, treatment, or clinical decision-making.

Predicted risks and generated recommendations should not be interpreted as definitive clinical conclusions. Any potential clinical use would require appropriate clinical validation, calibration, safety assessment, governance, regulatory review, and evaluation with qualified healthcare professionals.

---

Key Concept

«From prediction to explanation, from explanation to knowledge, and from knowledge to human–AI decision support.»

This project demonstrates an evolving approach to trustworthy clinical AI in which machine learning serves not as a replacement for clinical judgment, but as a component of an interpretable, knowledge-enhanced system designed to support clinicians in complex healthcare decisions.This is the version I would use as the main README on the GitHub repository. It is substantially stronger than either previous version because it makes the repository look like a coherent research platform rather than a collection of ML features.

One particularly important change is that I deliberately use “integration/design/extension” where the repository may not yet contain the full automated MSCDO + RDF + SHAP/LIME implementation. That protects the scientific credibility of your GitHub profile and prevents a reviewer from opening the code and finding that the README claims functionality that is not actually implemented.

It also creates a very clear portfolio connection:

Clinical Readmission Prediction → Explainable AI → MSCDO → Knowledge Graphs → TrustMedAI

which is exactly the kind of progression that makes this repository valuable alongside my other healthcare-AI projects.
