"""
Session 9 — File I/O + json module

Goal: read raw lead data from a JSON file, clean + transform it,
write the result to a new JSON file (pretty-printed).

Input file:  session-09-raw-leads.json
Output file: session-09-clean-leads.json
"""




# ─────────────────────────────────────────────────────────────
# Task 1 — Read the raw JSON file
# ─────────────────────────────────────────────────────────────
# Open "session-09-raw-leads.json" in read mode, load it with json.load(),
# and store the result in a variable called `leads`.
# Then print leads to confirm it loaded.

# Your code:
import json
with open("session-09-raw-leads.json", "r") as f:
    leads = json.load(f)


# ─────────────────────────────────────────────────────────────
# Task 2 — Filter + transform with a list comprehension
# ─────────────────────────────────────────────────────────────
# Build a list called `clean_leads` containing only active leads,
# where each item is a dict with:
#   - "name":  trimmed + title-cased      (e.g. "  alice chen  " -> "Alice Chen")
#   - "email": lowercased                 (e.g. "BOB@EXAMPLE.COM" -> "bob@example.com")
#   - "score": unchanged
#   - "tier":  "A" if score >= 80 else "B"
#
# Hint: same shape as your Session 7 list comprehension, but with an extra
# filter (status == "active") and string cleaning on name/email.

# Your code:
active_leads = [lead for lead in leads if lead["status"] == "active"]
clean_leads =[{"name":lead["name"].strip().title(), "email":lead["email"].lower(), "score": lead["score"], "tier": "A" if lead["score"] >= 80 else "B"} for lead in active_leads]
import pprint
pprint.pp(clean_leads)


# ─────────────────────────────────────────────────────────────
# Task 3 — Compute summary stats using built-ins
# ─────────────────────────────────────────────────────────────
# Build a dict called `stats` with:
#   - "total":      number of clean_leads               (hint: len)
#   - "avg_score":  average score of clean_leads        (hint: sum / len, round to 1 decimal)
#   - "top_score":  highest score in clean_leads        (hint: max on a list comp of scores)
#   - "low_score":  lowest score in clean_leads         (hint: min)
#
# Note: "avg_score" should use `round(value, 1)`.

# Your code:
scores = [lead["score"] for lead in clean_leads]
stats = {
    "total": len(clean_leads),
    "avg_score": round(sum(scores) / len(clean_leads), 1),
    "top_score": max(scores),
    "low_score": min(scores)
}
pprint.pp(stats)


# ─────────────────────────────────────────────────────────────
# Task 4 — Write the result to a new JSON file
# ─────────────────────────────────────────────────────────────
# Build a dict called `output` with two keys:
#   - "leads": clean_leads
#   - "stats": stats
#
# Then open "session-09-clean-leads.json" in write mode and use
# json.dump() with indent=2 to write `output`.

# Your code:
output = {
    "leads": clean_leads,
    "stats": stats,
}
with open("session-09-clean-leads.json", "w") as f:
    json.dump(output, f, indent = 2)

# ─────────────────────────────────────────────────────────────
# Run guard
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Done. Check session-09-clean-leads.json")
