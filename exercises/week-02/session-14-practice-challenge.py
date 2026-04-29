"""
Session 14 - Week 2 Practice Challenge

Goal: practice file I/O, filtering, normalization, summary building,
and main() orchestration in one small Python script.

Input file:
exercises/week-02/session-14-raw-tickets.json

Output file:
exercises/week-02/session-14-triage-output.json
"""

import json

INPUT_PATH = "exercises/week-02/session-14-raw-tickets.json"
OUTPUT_PATH = "exercises/week-02/session-14-triage-output.json"


def load_tickets(path):
    """
    Read the JSON file and return the parsed list of ticket dicts.
    """

    # Your code here
    with open(path, "r") as f:
        tickets = json.load(f)
    return(tickets)


def filter_triage_tickets(tickets):
    """
    Keep only tickets where:
    - status == "open"
    - priority is "high" or "urgent"
    - owner is not empty after strip()
    """

    # Your code here
    tickets = [
        ticket for ticket in tickets if
            ticket["status"] == "open" and
            (ticket["priority"] == "high" or 
            ticket["priority"] == "urgent") and
            ticket["owner"].strip()
    ]
    return tickets




def normalize_tickets(tickets):
    """
    Return a new list of dicts with this shape:
    {
        "id": original id,
        "owner": trimmed + lowercased owner,
        "team": original team,
        "priority": original priority
    }
    """

    # Your code here
    tickets = [{
        "id": ticket["id"],
        "owner": ticket["owner"].strip().lower(),
        "team": ticket["team"],
        "priority": ticket["priority"]
    } for ticket in tickets]
    return tickets



def build_summary(tickets):
    """
    Build and return:
    {
        "ticketCount": <count>,
        "byTeam": <dict counting tickets by team>,
        "urgentIds": <list of ids for urgent tickets>
    }
    """

    summary = {
        "ticketCount": 0,
        "byTeam": {},
        "urgentIds": [],
    }

    # Your code here
    for ticket in tickets:
        summary["ticketCount"] += 1
        if ticket["team"] not in summary["byTeam"]:
            summary["byTeam"][ticket["team"]] = 0
        summary["byTeam"][ticket["team"]] += 1
        if ticket["priority"] == "urgent":
            summary["urgentIds"].append(ticket["id"])

    return summary


def main():
    tickets = load_tickets(INPUT_PATH)
    triage_tickets = filter_triage_tickets(tickets)
    normalized = normalize_tickets(triage_tickets)
    summary = build_summary(normalized)

    output = {
        "tickets": normalized,
        "summary": summary,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(summary)


if __name__ == "__main__":
    main()
