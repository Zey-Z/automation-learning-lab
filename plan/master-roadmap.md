# Master Roadmap — 6-Week Automation Engineering Program

---

## Week 1: JavaScript Foundations + Shell / Terminal / Environment

### Concepts
- Terminal vs shell (bash, PowerShell, cmd)
- Absolute vs relative paths
- Environment variables and PATH
- JavaScript: variables, data types, let/const, type coercion
- Control flow: if/else, ternary, switch, for, while, for...of
- Arrays: access, iterate, mutate
- Objects: access, destructure, spread
- JSON: parse, stringify, nested access

### Drills
- Variable declaration and type checking
- Conditionals and loops
- Array methods: `.map()`, `.filter()`, `.find()`, `.reduce()`, `.some()`, `.every()`
- Object manipulation: access, destructure, merge, nested access
- JSON parsing and field extraction

### Coding task
Clean and normalize a batch of lead records: trim whitespace, lowercase emails, validate required fields, split into `{ cleaned: [], rejected: [] }`

### Automation task
Build a data pipeline script: read a JSON file → validate each record → transform fields → write cleaned output to a new file

### Deliverables
- `submissions/week-01/exercise-01-lead-normalizer.js`
- `submissions/week-01/exercise-02-data-pipeline.js`
- `feedback/week-01/` review notes

### Mastery criteria
- Can declare variables and explain let vs const
- Can use `.map()`, `.filter()`, `.reduce()` correctly without looking up syntax
- Can parse JSON, access nested fields, and handle missing keys
- Can read an error message and identify whether it is a type error, reference error, or syntax error
- Lead normalizer handles edge cases: empty strings, missing fields, duplicate emails

---

## Week 2: HTTP, REST, APIs, Status Codes, Headers + Python Fundamentals

### Concepts
- HTTP methods: GET, POST, PUT, PATCH, DELETE — when to use each
- Status codes: 2xx success, 4xx client error, 5xx server error
- Headers: Content-Type, Authorization, Accept
- Request body vs query parameters
- REST API conventions: resources, endpoints, CRUD mapping
- Python basics: variables, types, functions, lists, dicts, tuples
- Python for automation: file I/O, `json` module, `requests` library

### Drills
- Match HTTP methods to CRUD operations
- Read a status code and explain what went wrong
- Parse API response payloads (JS)
- Python: list comprehensions, dict operations, function writing
- Python: read/write JSON files, make HTTP requests with `requests`

### Coding task
JS: Fetch data from a public API, extract specific fields, handle errors, format output as clean JSON

### Automation task
Python: Write a script that calls an API → parses the response → filters/transforms records → saves structured results to a file

### Deliverables
- `submissions/week-02/exercise-01-api-fetch.js`
- `submissions/week-02/exercise-02-python-api-script.py`
- `feedback/week-02/` review notes

### Mastery criteria
- Can explain GET vs POST vs PUT vs PATCH vs DELETE with real examples
- Can read a 401, 403, 404, 429 status and explain the cause
- Can construct an API request with correct headers and body
- Can write a Python function that takes input, processes it, and returns output
- Python script handles: missing keys in response, non-200 status, file write errors

---

## Week 3: SQL Deep Dive

### Concepts
- Table, row, column, primary key — what each means and why
- Schema: defining structure before data exists
- Data types in SQL: TEXT, INTEGER, BOOLEAN, TIMESTAMP
- Validation: NOT NULL, UNIQUE, CHECK constraints
- Normalization: why split data into multiple tables (1NF, 2NF, 3NF conceptual)
- Deduplication: identifying and handling duplicate records
- Upsert: INSERT ... ON CONFLICT UPDATE (PostgreSQL syntax)
- SELECT, WHERE, ORDER BY, LIMIT
- JOIN: INNER JOIN, LEFT JOIN — when and why
- INSERT, UPDATE, DELETE
- Aggregate functions: COUNT, SUM, AVG, GROUP BY, HAVING

### Drills
- Write SELECT queries with WHERE, ORDER BY, LIMIT
- Write JOIN queries across 2 tables
- Write INSERT and UPDATE statements
- Write an upsert statement
- Identify duplicate records with GROUP BY + HAVING
- Design a simple schema for a given business scenario

### Coding task
Given a messy CSV of contact records: write SQL to create the schema, insert records, deduplicate by email, and query for specific segments (e.g., all contacts from a certain domain, contacts missing phone numbers)

### Automation task
Build a JS or Python script that: reads raw data → validates against schema rules → inserts into SQLite → runs dedup logic → exports clean results

### Deliverables
- `submissions/week-03/exercise-01-sql-queries.sql`
- `submissions/week-03/exercise-02-schema-design.sql`
- `submissions/week-03/exercise-03-data-pipeline.js` or `.py`
- `feedback/week-03/` review notes

### Mastery criteria
- Can design a 2-3 table schema with primary keys and foreign keys
- Can write SELECT with WHERE, JOIN, GROUP BY without reference
- Can explain why normalization matters with a concrete example
- Can write an upsert and explain when it is needed
- Can identify duplicates in a dataset using SQL
- Data pipeline script validates input before inserting

---

## Week 4: Webhooks + Auth + Reliability Basics

### Concepts
- Webhooks: how event-driven push works vs polling
- Webhook payloads: parsing, validating required fields, signature verification (conceptual)
- Auth: API keys, bearer tokens, JWT structure (header.payload.signature), OAuth2 flow (conceptual)
- Retry: why requests fail, when to retry, max attempts
- Backoff: linear vs exponential, jitter
- Fallback: what to do when retries are exhausted
- Idempotency: why the same request twice should not create duplicate effects
- Logging: what to log (input, output, errors, timing), structured logging basics
- Debugging: reading error messages, stack traces, using console/print for tracing

### Drills
- Parse a webhook payload and extract event type + relevant fields
- Construct an Authorization header with a bearer token
- Decode a JWT payload (base64) and read the claims
- Write a retry function with exponential backoff
- Write a function that logs input, output, and errors in structured format

### Coding task
Build a webhook payload handler: receive event JSON → validate required fields → route to different handlers based on event type → log every step

### Automation task
Build a reliable API caller: make a request → if it fails, retry with exponential backoff → if retries exhausted, log failure and execute fallback → ensure idempotency by checking for duplicate event IDs

### Deliverables
- `submissions/week-04/exercise-01-webhook-handler.js`
- `submissions/week-04/exercise-02-reliable-api-caller.js`
- `feedback/week-04/` review notes

### Mastery criteria
- Can explain webhook vs polling with a real scenario
- Can parse a JWT without a library and explain each part
- Can implement retry with exponential backoff from scratch
- Can explain idempotency and why it matters for webhooks
- Webhook handler validates input and logs every decision point
- Reliable API caller handles: timeout, 429, 500, network error

---

## Week 5: End-to-End Automation Build

### Concepts
- Composing multiple skills into one pipeline
- Data flow: trigger → validate → transform → call → store → output
- Error boundaries: where to catch, where to let fail
- State management: tracking what has been processed
- Testing your automation: manual verification, edge case testing

### Drills
- Trace data through a multi-step pipeline on paper
- Identify where errors could occur in a given pipeline diagram
- Write validation functions for different input shapes
- Write transform functions that normalize between two different API schemas

### Coding task
Build: webhook trigger → validate payload → transform data → call external API → store result in SQLite → output summary or send notification (console/file)

### Automation task
Add reliability to the pipeline: retry failed API calls, log every step, handle partial failures (some records succeed, some fail), produce a summary report of what succeeded and what failed

### Deliverables
- `submissions/week-05/e2e-automation.js` (or split into modules)
- `submissions/week-05/test-scenarios.md` (edge cases tested and results)
- `projects/mini-04-e2e-automation/` — polished version
- `feedback/week-05/` review notes

### Mastery criteria
- Pipeline runs end-to-end without manual intervention
- Handles at least 3 failure scenarios gracefully (bad input, API down, DB write error)
- Every step logs what it received and what it produced
- Partial failures do not crash the whole pipeline
- Can explain the data flow from trigger to output without looking at code

---

## Week 6: Documentation, Handoff, Training + Portfolio Polish

### Concepts
- README: what it covers, who it is for, what makes a good one
- Setup guide: environment requirements, install steps, configuration
- Runbook: how to operate, monitor, and troubleshoot the automation
- Troubleshooting note: common failure modes and how to resolve them
- Training/handoff note: what a new person needs to know to take over
- Delivery quality: the difference between "it works" and "it is ready to hand off"

### Drills
- Write a README for one of your earlier projects from scratch
- Write a troubleshooting section: given 3 failure scenarios, document cause and fix
- Write a setup guide for your week 5 project
- Peer-review exercise: read your own code from week 1 and document what is unclear

### Coding task
Go back to your week 5 project and refactor for clarity: rename unclear variables, add minimal comments where logic is non-obvious, ensure consistent error handling

### Automation task
Create a complete documentation bundle for your week 5 project:
1. README.md — what it does, how to run it, what it depends on
2. SETUP.md — step-by-step environment and dependency setup
3. RUNBOOK.md — how to operate, what to monitor, how to restart
4. TROUBLESHOOTING.md — known failure modes and fixes
5. HANDOFF.md — what a new person needs to know, key decisions made, what to watch for

### Deliverables
- `projects/mini-05-documentation-bundle/README.md`
- `projects/mini-05-documentation-bundle/SETUP.md`
- `projects/mini-05-documentation-bundle/RUNBOOK.md`
- `projects/mini-05-documentation-bundle/TROUBLESHOOTING.md`
- `projects/mini-05-documentation-bundle/HANDOFF.md`
- `submissions/week-06/refactored-project/` — cleaned week 5 code
- `feedback/week-06/` review notes

### Mastery criteria
- README is understandable by someone who has never seen the project
- Setup guide works: following it from scratch produces a running system
- Runbook covers: normal operation, monitoring, restart procedure
- Troubleshooting covers at least 3 real failure modes encountered during development
- Handoff note explains key design decisions, not just instructions
- Code refactor improves clarity without changing behavior

---

## Final Portfolio Outputs

By the end of week 6, the student should have these 6 concrete artifacts:

| # | Artifact | Source | Location |
|---|----------|--------|----------|
| 1 | JS data normalization / transformation project | Week 1 | `submissions/week-01/` |
| 2 | API integration script (JS + Python) | Week 2 | `submissions/week-02/` |
| 3 | SQL schema / validation / query exercise set | Week 3 | `submissions/week-03/` |
| 4 | Webhook + reliability project | Week 4 | `submissions/week-04/` |
| 5 | End-to-end automation project | Week 5 | `projects/mini-04-e2e-automation/` |
| 6 | Documentation bundle (README + runbook + handoff) | Week 6 | `projects/mini-05-documentation-bundle/` |

Each artifact should be polished enough to show in a job interview or include in a portfolio.
Final polished versions go in `submissions/portfolio/`.
