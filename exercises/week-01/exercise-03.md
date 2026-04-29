# Exercise 03 — Lead Pipeline (Week 1 Capstone)

## Scenario
You work on a marketing automation team. Every morning, raw lead data is dumped into a JSON file. Your job: read it, clean it, filter it, summarize it, and write the results to a new file.

## Input
File: `exercises/week-01/raw-leads.json`

## Task
Create `exercises/week-01/exercise-03.js` that does the following:

### Step 1: Read + Parse
Read `raw-leads.json` and parse it into an array of objects.

### Step 2: Validate
Filter out invalid leads. A lead is **invalid** if:
- `name` is empty (after trimming)
- `email` is empty (after trimming)

### Step 3: Filter
From the valid leads, keep only leads where:
- `status` is `"active"`
- `score` >= 50

### Step 4: Transform
For each remaining lead, create a new object:
```js
{
  name: "Alice Chen",           // original name
  email: "alice@acme.com",      // trimmed + lowercase
  company: "Acme Corp",         // original
  score: 85                     // original
}
```

### Step 5: Summarize
Create a summary object:
```js
{
  totalLeads: 3,                    // how many leads passed all filters
  averageScore: 77,                 // average score (rounded to nearest integer)
  companyCounts: {                  // count leads per company
    "Acme Corp": 2,
    "TestCo": 1
  },
  topLead: "Dan Lee"                // name of the lead with highest score
}
```

### Step 6: Write output
Write a file `exercises/week-01/lead-output.json` containing:
```js
{
  "leads": [ ...transformed leads array... ],
  "summary": { ...summary object... }
}
```

## Requirements
- Use `fs.readFileSync` and `fs.writeFileSync`
- Use `JSON.parse` and `JSON.stringify`
- Use `.filter()`, `.map()`, `.reduce()` — no for loops
- Write it as multiple named functions, not one giant block

## Rubric
- Correctness: output file matches expected (5 pts)
- Uses array methods properly (2 pts)
- Code organized into functions (2 pts)
- Handles dirty data (trimming, lowercase) (1 pt)
