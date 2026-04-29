# Session 8 — Dict Methods + Dict Comprehension Exercise
# Objective: Use .items(), .get(), and dict comprehensions on lead data

leads = [
    {"name": "Alice Wong",  "score": 82, "region": "north"},
    {"name": "Bob Smith",   "score": 55, "region": "south"},
    {"name": "Carol Chen",  "score": 91, "region": "north"},
    {"name": "David Park",  "score": 47, "region": "south"},
    {"name": "Eve Harris",  "score": 73, "region": "east"},
]

# Task 1
# Build a dict mapping each lead's name to their score.
# Expected: {"Alice Wong": 82, "Bob Smith": 55, ...}
name_to_score = {lead["name"]:lead["score"] for lead in leads}

print("Task 1:", name_to_score)

# Task 2
# Build a dict mapping each lead's name to their tier.
# Tier: "A" if score >= 80, else "B"
# Expected: {"Alice Wong": "A", "Bob Smith": "B", ...}
name_to_tier = {lead["name"]: "A" if lead["score"] >= 80 else "B" for lead in leads}

print("Task 2:", name_to_tier)

# Task 3
# Build a dict grouping names by region.
# Expected: {"north": ["Alice Wong", "Carol Chen"], "south": [...], "east": [...]}
# Hint: this one cannot be done in a single dict comprehension.
#       Use a regular for loop + dict to accumulate.
by_region = {}
for lead in leads:
    region = lead["region"]

    if region not in by_region:
        by_region[region] = []
    
    by_region[region].append(lead["name"])


print("Task 3:", by_region)
