from lime.lime_tabular import LimeTabularExplainer



def create_lime_explanation(
        model,
        X_train,
        X_patient
):


    explainer = LimeTabularExplainer(
        X_train.values,
        feature_names=X_train.columns,
        class_names=[
            "No Readmission",
            "Readmission"
        ],
        mode="classification"
    )


    explanation = explainer.explain_instance(
        X_patient.values[0],
        model.predict_proba,
        num_features=10
    )


    return explanation
