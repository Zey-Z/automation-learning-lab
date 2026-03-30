# Master Roadmap — 6-Week Automation Engineering Program

Planning unit: content blocks per session (not days). Adjust density based on actual pace.

---

## Week 1: JavaScript Foundations + Shell / Terminal / Environment

### Block A: Environment Basics
- Terminal vs shell (bash, PowerShell, cmd)
- Absolute vs relative paths
- Environment variables and PATH

### Block B: JS Core
- Variables, data types, let/const, type coercion
- Control flow: if/else, ternary, switch, for, while, for...of
- Truthy/falsy values

### Block C: Arrays + Array Methods
- `.filter()`, `.map()`, `.find()`, `.reduce()`, `.some()`, `.every()`
- 10-question drill per method group (5 basic + 5 variant)
- Memorization passes until independent fluency

### Block D: Objects + JSON
- Object access, destructuring, spread operator
- JSON: parse, stringify, nested access, missing key handling
- 10-question drill (5 basic + 5 variant)

### Block E: Applied Coding
- Exercise: clean and normalize lead data using filter + map
- Exercise: data pipeline — read JSON → validate → transform → write output
- New skill: `fs` module (file I/O)

### Block F: Practice Block (~2 hours)
- Mixed drills across all Block A–D skills
- Timed exercises and memorization
- New-scenario drills to test independent application

### Deliverables
- `submissions/week-01/exercise-01-lead-normalizer.js`
- `submissions/week-01/exercise-02-data-pipeline.js`
- `feedback/week-01/` review notes

### Mastery criteria
- Use .filter(), .map(), .reduce() without reference
- Parse JSON and handle missing keys
- Identify error types from error messages
- Can write a complete data cleaning function independently in a new scenario

---

## Week 2: HTTP, REST, APIs, Status Codes, Headers + Python Fundamentals

### Block A: HTTP Fundamentals
- HTTP methods: GET, POST, PUT, PATCH, DELETE — when to use each
- Status codes: 2xx success, 4xx client error, 5xx server error
- Headers: Content-Type, Authorization, Accept
- Request body vs query parameters

### Block B: REST + API Calls in JS
- REST conventions: resources, endpoints, CRUD mapping
- Making API calls with fetch or node-fetch
- Reading and parsing API responses
- Error handling for API calls

### Block C: Python Fundamentals
- Variables, types, functions, lists, dicts, tuples
- List comprehensions, dict operations
- File I/O, `json` module
- `requests` library for API calls

### Block D: Drills (10 each)
- HTTP methods + status codes drill (5 basic + 5 variant)
- API response parsing drill (5 basic + 5 variant)
- Python basics drill (5 basic + 5 variant)

### Block E: Applied Coding
- JS: Fetch from public API, extract fields, handle errors, format output
- Python: Call API → parse response → filter/transform → save to file

### Block F: Practice Block (~2 hours)
- Mixed JS + Python drills
- API debugging exercises (given broken requests, find the bug)
- Timed coding challenges

### Deliverables
- `submissions/week-02/exercise-01-api-fetch.js`
- `submissions/week-02/exercise-02-python-api-script.py`
- `feedback/week-02/` review notes

### Mastery criteria
- Explain GET vs POST vs PUT vs PATCH vs DELETE with real examples
- Read a 401, 403, 404, 429 status and explain the cause
- Construct an API request with correct headers and body
- Write a Python function that takes input, processes it, and returns output
- Python script handles: missing keys, non-200 status, file write errors

---

## Week 3: SQL Deep Dive

### Block A: Foundations
- Table, row, column, primary key, foreign key
- Schema: defining structure before data exists
- Data types: TEXT, INTEGER, BOOLEAN, TIMESTAMP

### Block B: Constraints + Normalization
- Validation: NOT NULL, UNIQUE, CHECK constraints
- Normalization: 1NF, 2NF, 3NF (conceptual, with concrete examples)
- Why split data into multiple tables

### Block C: Queries
- SELECT, WHERE, ORDER BY, LIMIT
- JOIN: INNER JOIN, LEFT JOIN — when and why
- Aggregate functions: COUNT, SUM, AVG, GROUP BY, HAVING
- INSERT, UPDATE, DELETE

### Block D: Advanced Operations
- Deduplication: identify duplicates with GROUP BY + HAVING
- Upsert: INSERT ... ON CONFLICT UPDATE
- Schema design for a business scenario

### Block E: Drills (10 each)
- SELECT + WHERE + JOIN drill (5 basic + 5 variant)
- Schema design drill (5 basic + 5 variant)
- Dedup + upsert drill (5 basic + 5 variant)

### Block F: Applied Coding
- Given messy CSV: create schema, insert, deduplicate by email, query segments
- JS or Python script: read raw data → validate → insert into SQLite → dedup → export

### Block G: Practice Block (~2 hours)
- Timed SQL query writing
- Schema design under time pressure
- Mixed drill: given a business scenario, design schema + write queries

### Deliverables
- `submissions/week-03/exercise-01-sql-queries.sql`
- `submissions/week-03/exercise-02-schema-design.sql`
- `submissions/week-03/exercise-03-data-pipeline.js` or `.py`
- `feedback/week-03/` review notes

### Mastery criteria
- Design a 2-3 table schema with primary keys and foreign keys
- Write SELECT with WHERE, JOIN, GROUP BY without reference
- Explain normalization with a concrete example
- Write an upsert and explain when it is needed
- Identify duplicates in a dataset using SQL

---

## Week 4: Webhooks + Auth + Reliability Basics

### Block A: Webhooks
- How event-driven push works vs polling
- Webhook payloads: parsing, validating required fields
- Signature verification (conceptual)

### Block B: Auth
- API keys, bearer tokens
- JWT structure: header.payload.signature
- OAuth2 flow (conceptual)

### Block C: Reliability
- Retry: why requests fail, when to retry, max attempts
- Backoff: linear vs exponential, jitter
- Fallback: what to do when retries exhausted
- Idempotency: why same request twice should not create duplicates

### Block D: Logging + Debugging
- What to log: input, output, errors, timing
- Structured logging basics
- Reading error messages, stack traces

### Block E: Drills (10 each)
- Webhook payload parsing drill (5 basic + 5 variant)
- Auth header construction drill (5 basic + 5 variant)
- Retry + idempotency drill (5 basic + 5 variant)

### Block F: Applied Coding
- Webhook handler: receive JSON → validate → route by event type → log every step
- Reliable API caller: request → retry with exponential backoff → fallback → idempotency check

### Block G: Practice Block (~2 hours)
- Mixed reliability drills
- Debugging exercises: find bugs in broken webhook handlers
- Timed implementation: write retry logic from scratch

### Deliverables
- `submissions/week-04/exercise-01-webhook-handler.js`
- `submissions/week-04/exercise-02-reliable-api-caller.js`
- `feedback/week-04/` review notes

### Mastery criteria
- Explain webhook vs polling with a real scenario
- Parse a JWT without a library and explain each part
- Implement retry with exponential backoff from scratch
- Explain idempotency and why it matters for webhooks
- Webhook handler validates input and logs every decision point

---

## Week 5: End-to-End Automation Build

### Block A: Pipeline Design
- Composing multiple skills into one pipeline
- Data flow: trigger → validate → transform → call → store → output
- Error boundaries: where to catch, where to let fail

### Block B: Implementation
- Build: webhook trigger → validate → transform → API call → store in SQLite → output summary
- Add reliability: retry failed calls, log every step, handle partial failures

### Block C: Testing + Edge Cases
- Manual verification, edge case testing
- State management: tracking what has been processed
- Summary report: what succeeded, what failed

### Block D: Drills (10 each)
- Pipeline tracing drill (5 basic + 5 variant)
- Error boundary drill (5 basic + 5 variant)

### Block E: Practice Block (~2 hours)
- Timed end-to-end builds
- Debugging broken pipelines
- Adding features to existing pipelines under time pressure

### Deliverables
- `submissions/week-05/e2e-automation.js`
- `submissions/week-05/test-scenarios.md`
- `projects/mini-04-e2e-automation/` — polished version
- `feedback/week-05/` review notes

### Mastery criteria
- Pipeline runs end-to-end without manual intervention
- Handles at least 3 failure scenarios gracefully
- Every step logs what it received and what it produced
- Partial failures do not crash the whole pipeline
- Can explain the data flow from trigger to output without looking at code

---

## Week 6: Documentation, Handoff, Training + Portfolio Polish

### Block A: Documentation Skills
- README: what it covers, who it is for
- Setup guide: environment, install, configuration
- Runbook: operate, monitor, troubleshoot
- Training/handoff note: what a new person needs to take over

### Block B: Writing Practice
- Write README for week 5 project
- Write setup guide, runbook, troubleshooting note, handoff note
- Peer-review exercise: read own code from week 1, document what is unclear

### Block C: Code Refactoring
- Refactor week 5 project for clarity: rename, comment non-obvious logic, consistent error handling
- Delivery quality: the difference between "it works" and "it is ready to hand off"

### Block D: Drills (10 each)
- Documentation writing drill (5 basic + 5 variant)
- Code reading + explanation drill (5 basic + 5 variant)

### Block E: Practice Block (~2 hours)
- Timed documentation writing
- Mock handoff exercise: explain a project to a "new team member" (the tutor asks questions)
- Final review of all portfolio artifacts

### Deliverables
- `projects/mini-05-documentation-bundle/README.md`
- `projects/mini-05-documentation-bundle/SETUP.md`
- `projects/mini-05-documentation-bundle/RUNBOOK.md`
- `projects/mini-05-documentation-bundle/TROUBLESHOOTING.md`
- `projects/mini-05-documentation-bundle/HANDOFF.md`
- `submissions/week-06/refactored-project/`
- `feedback/week-06/` review notes

### Mastery criteria
- README is understandable by someone who has never seen the project
- Setup guide works: following from scratch produces a running system
- Runbook covers: normal operation, monitoring, restart procedure
- Troubleshooting covers at least 3 real failure modes encountered during development
- Handoff note explains key design decisions, not just instructions

---

## Final Portfolio Outputs

| # | Artifact | Source | Location |
|---|----------|--------|----------|
| 1 | JS data normalization / transformation project | Week 1 | `submissions/week-01/` |
| 2 | API integration script (JS + Python) | Week 2 | `submissions/week-02/` |
| 3 | SQL schema / validation / query exercise set | Week 3 | `submissions/week-03/` |
| 4 | Webhook + reliability project | Week 4 | `submissions/week-04/` |
| 5 | End-to-end automation project | Week 5 | `projects/mini-04-e2e-automation/` |
| 6 | Documentation bundle (README + runbook + handoff) | Week 6 | `projects/mini-05-documentation-bundle/` |

Each artifact should be polished enough to show in a job interview.
Final polished versions go in `submissions/portfolio/`.
