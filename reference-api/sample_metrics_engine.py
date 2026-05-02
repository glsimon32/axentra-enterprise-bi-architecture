"""
Sanitized reference metrics engine for an enterprise BI platform.

This file is for portfolio demonstration only.
It does not include production Axentra source code, proprietary logic,
customer data, database schema, prompts, credentials, or internal workflows.
"""

from collections import Counter


mock_metrics = [
    {
        "sourceSystem": "HRMS",
        "businessFunction": "Human Resources",
        "department": "Operations",
        "metricName": "Employee Attrition Rate",
        "metricValue": 8.4,
        "metricUnit": "percentage",
        "riskLevel": "medium",
    },
    {
        "sourceSystem": "Asset Management",
        "businessFunction": "IT Operations",
        "department": "Technology",
        "metricName": "Pending Asset Allocation Requests",
        "metricValue": 42,
        "metricUnit": "count",
        "riskLevel": "high",
    },
    {
        "sourceSystem": "ITSM",
        "businessFunction": "Service Operations",
        "department": "IT Support",
        "metricName": "Average Resolution Time",
        "metricValue": 18.5,
        "metricUnit": "hours",
        "riskLevel": "medium",
    },
]


def summarize_metrics(metrics):
    total_metrics = len(metrics)
    risk_distribution = Counter(item["riskLevel"] for item in metrics)
    source_systems = sorted({item["sourceSystem"] for item in metrics})

    return {
        "totalMetrics": total_metrics,
        "sourceSystems": source_systems,
        "riskDistribution": dict(risk_distribution),
    }


def generate_executive_summary(metrics):
    high_risk_items = [item for item in metrics if item["riskLevel"] == "high"]

    if not high_risk_items:
        return "No high-risk enterprise metrics require immediate leadership attention."

    names = ", ".join(item["metricName"] for item in high_risk_items)

    return (
        f"{len(high_risk_items)} high-risk metric requires leadership attention: "
        f"{names}."
    )


if __name__ == "__main__":
    print(summarize_metrics(mock_metrics))
    print(generate_executive_summary(mock_metrics))
