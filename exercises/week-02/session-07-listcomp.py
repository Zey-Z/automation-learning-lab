# Session 7 — List Comprehension Exercise
# Objective: Practice filter + transform using Python list comprehensions

leads = [
    {"name": "alice wong",   "status": "active",   "score": 82},
    {"name": "bob smith",    "status": "inactive", "score": 55},
    {"name": "carol chen",   "status": "active",   "score": 91},
    {"name": "david park",   "status": "active",   "score": 47},
    {"name": "  eve harris", "status": "active",   "score": 73},
]

# Task 1 — Filter
# Keep only leads where status == "active"
# Return a list of the original dicts (no changes)
active_leads = [lead for lead in leads if lead["status"] == "active"]

print("Task 1:", active_leads)

# Task 2 — Transform
# From active_leads, produce a new list of dicts with this shape:
#   {"name": "Alice Wong", "score": 82, "tier": "A"}
# Rules:
#   - name → strip whitespace + title case
#   - score → unchanged
#   - tier → "A" if score >= 80, else "B"
summaries = [{"name" :lead["name"].strip().title(), "score" : lead["score"], "tier" : "A" if lead["score"] >= 80 else "B"} for lead in active_leads]

print("Task 2:", summaries)
