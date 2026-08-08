"""
Mapping ML outputs to MSCDO concepts
"""


HIGH_RISK = 0.75
MODERATE_RISK = 0.40



def map_readmission_risk(probability):


    if probability >= HIGH_RISK:

        return {
            "risk_class":
            "msdo:HighRiskProfile",

            "recommendation":
            "msdo:EnhancedMonitoring"
        }


    elif probability >= MODERATE_RISK:

        return {

            "risk_class":
            "msdo:ModerateRiskProfile",

            "recommendation":
            "msdo:ClinicalReview"

        }


    else:

        return {

            "risk_class":
            "msdo:LowRiskProfile",

            "recommendation":
            "msdo:RoutineFollowUp"

        }
