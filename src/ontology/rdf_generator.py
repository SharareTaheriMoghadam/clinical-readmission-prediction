from rdflib import Graph, Namespace, RDF



MSDO = Namespace(
"http://example.org/msdo#"
)



def create_patient_risk_instance(
        patient_id,
        risk_class
):


    graph = Graph()


    patient = MSDO[patient_id]


    graph.add(
        (
        patient,
        RDF.type,
        MSDO.Patient
        )
    )


    graph.add(
        (
        patient,
        MSDO.hasRiskProfile,
        MSDO[risk_class]
        )
    )


    return graph



def save_graph(graph,path):

    graph.serialize(
        destination=path,
        format="turtle"
    )
