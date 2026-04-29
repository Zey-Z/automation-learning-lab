"""
Session 12 - Python Lead Pipeline Reimplementation

Goal: re-implement the Week 1 JavaScript lead pipeline in Python.

Input file:
exercises/week-01/raw-leads.json

Output file:
exercises/week-02/session-12-lead-output.json
"""

import json

INPUT_PATH = "exercises/week-01/raw-leads.json"
OUTPUT_PATH = "exercises/week-02/session-12-lead-output.json"


def load_leads(path):
    """
    Read the JSON file and return the parsed list of lead dicts.
    """

    # Your code:
    with open(path, "r") as f:
        leads= json.load(f)
        return leads



def filter_valid_leads(leads):
    """
    Keep only leads where:
    - name is not empty after strip()
    - email is not empty after strip()
    """

    # Your code:
    valid_leads = [lead for lead in leads if lead["name"].strip() and lead["email"].strip()]
    return valid_leads

def filter_active_high_score(leads):
    """
    Keep only leads where:
    - status == "active"
    - score >= 50
    """

    # Your code:
    qualified_leads = [lead for lead in leads if lead["status"]== "active" and lead["score"]>=50]
    return qualified_leads



def transform_leads(leads):
    """
    Return a new list of dicts with this shape:
    {
        "name": original name,
        "email": trimmed + lowercased email,
        "company": original company,
        "score": original score
    }
    """

    # Your code:
    transformed= [{
        "name": lead["name"],
        "email": lead["email"].strip().lower(),
        "company": lead["company"],
        "score": lead["score"]
    } for lead in leads]
    return transformed


def summarize_leads(leads):
    """
    Build and return:
    {
        "totalLeads": <count>,
        "averageScore": <rounded average>,
        "companyCounts": <dict counting leads by company>,
        "topLead": <name of the highest-score lead>
    }
    """

    summary = {
        "totalLeads": 0,
        "averageScore": 0,
        "companyCounts": {},
        "topLead": "",
    }

    # Your code:
    highest = 0
    scores = [lead["score"] for lead in leads]
    for lead in leads:
        summary["totalLeads"] += 1
        summary["averageScore"] = round(sum(scores)/len(leads))
        if lead["company"] not in summary["companyCounts"]:
            summary["companyCounts"][lead["company"]] = 0
        summary["companyCounts"][lead["company"]] += 1
        if lead["score"] > highest:
            highest = lead["score"]
            summary["topLead"] = lead["name"]

    return summary


def main():
    leads = load_leads(INPUT_PATH)
    valid_leads = filter_valid_leads(leads)
    qualified_leads = filter_active_high_score(valid_leads)
    transformed = transform_leads(qualified_leads)
    summary = summarize_leads(transformed)

    output = {
        "leads": transformed,
        "summary": summary,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(summary)


if __name__ == "__main__":
    main()
