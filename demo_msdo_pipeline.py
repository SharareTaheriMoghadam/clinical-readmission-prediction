from ontology.msdo_mapping import *
from ontology.rdf_generator import *


# ML output

prediction_probability = 0.82



risk = map_readmission_risk(
    prediction_probability
)



graph=create_patient_risk_instance(
    "Patient001",
    risk["risk_class"]
)



save_graph(
    graph,
    "outputs/patient001.ttl"
)



print(
"MSCDO semantic decision artifact generated"
)
