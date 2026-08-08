"""
SHAP-based explainability module
for clinical readmission prediction
"""

import shap
import matplotlib.pyplot as plt


def generate_shap_explanation(model, X_patient):

    """
    Generate patient-level explanation
    """

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(
        X_patient
    )

    return shap_values



def save_shap_plot(model, X_patient, output):

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(
        X_patient
    )

    shap.force_plot(
        explainer.expected_value,
        shap_values,
        X_patient,
        matplotlib=True
    )

    plt.savefig(output)
