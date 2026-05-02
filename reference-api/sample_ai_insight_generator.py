"""
Sanitized reference AI insight generator for an enterprise BI platform.

This file is for portfolio demonstration only.
It does not call external AI providers.
It does not include production prompts, customer data, credentials,
database schema, agent workflows, or proprietary Axentra logic.
"""


def classify_risk(metric):
    value = metric.get("metricValue", 0)
    metric_name = metric.get("metricName", "").lower()

    if "pending" in metric_name and value >= 40:
        return "high"

    if "resolution" in metric_name and value >= 16:
        return "medium"

    if "attrition" in metric_name and value >= 8:
        return "medium"

    return "low"


def generate_insight(metric):
    risk = classify_risk(metric)

    return {
        "metricName": metric.get("metricName"),
        "sourceSystem": metric.get("sourceSystem"),
        "riskLevel": risk,
        "insight": (
            f"{metric.get('metricName')} from {metric.get('sourceSystem')} "
            f"is classified as {risk} risk based on sanitized reference rules."
        ),
        "recommendedAction": (
            "Review this metric with the accountable business owner."
            if risk in ["medium", "high"]
            else "Continue monitoring through the regular dashboard cycle."
        ),
    }


if __name__ == "__main__":
    sample_metric = {
        "sourceSystem": "Asset Management",
        "metricName": "Pending Asset Allocation Requests",
        "metricValue": 42,
    }

    print(generate_insight(sample_metric))
