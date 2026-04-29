# Session 13 - Gap Closing + API Mapping

**Goal:** close the main Week 2 gaps before the full practice block.
**Target time:** ~90 minutes
**Deliverables:**
- `question-bank/week-02/rest-collections-drill-01.md`
- `question-bank/week-02/session-13-main-memorization.md`
- `exercises/week-02/session-13-js-fetch.js`
- `exercises/week-02/session-13-main-wiring.py`

---

## Part 1 - Venv mini lab (~15 min)

Run these commands in PowerShell from the repo root:

```powershell
python -m venv .venv-session13
.\.venv-session13\Scripts\Activate.ps1
python --version
pip --version
deactivate
```

Optional if network is available:

```powershell
.\.venv-session13\Scripts\Activate.ps1
pip install requests
python -c "import requests; print(requests.__version__)"
deactivate
```

**What to notice:**
1. `python -m venv ...` creates an isolated environment folder.
2. Activation changes which Python and `pip` your terminal uses.
3. `deactivate` returns you to the global environment.

---

## Part 2 - REST quick map (~15 min)

Use these scenarios for quick oral or written recall:

- Read one user by id -> `GET /users/123`
- Create a new order -> `POST /orders`
- Replace one task completely -> `PUT /tasks/9`
- Update one field only -> `PATCH /tasks/9`
- Delete one webhook -> `DELETE /webhooks/2`

**Checkpoint:** explain the difference between:
- resource
- endpoint
- collection endpoint
- single-item endpoint

---

## Part 3 - Collections gap closing (~15 min)

Make sure these Python shapes are comfortable:

- list indexing: `items[0]`, `items[-1]`
- slicing: `items[1:4]`
- append one item: `items.append(x)`
- extend with another list: `items.extend(other_items)`
- safe dict lookup: `lead.get("score", 0)`
- dict view methods: `data.keys()`, `data.values()`
- tuple = ordered and immutable

Then complete:
- `question-bank/week-02/rest-collections-drill-01.md`

---

## Part 4 - JS fetch side-by-side (~20 min)

Complete:
- `exercises/week-02/session-13-js-fetch.js`

**Focus only on mapping:**
- `requests.get(...)` <-> `fetch(...)`
- `params={...}` <-> URL query string / `searchParams`
- `response.status_code` <-> `response.status`
- `response.json()` in Python <-> `await response.json()` in JS
- output file writing still happens locally with `fs.writeFileSync(...)`

Run:

```powershell
node exercises/week-02/session-13-js-fetch.js
```

---

## Part 5 - Main wiring drill (~20 min)

Complete:
- `exercises/week-02/session-13-main-wiring.py`

The helper functions are already written. The learning target is:
- read `main()`
- track data flow line by line
- connect helper outputs to the next helper input
- keep orchestration separate from helper logic

Run:

```powershell
python exercises/week-02/session-13-main-wiring.py
```

Then complete:
- `question-bank/week-02/session-13-main-memorization.md`

---

## End-of-session checklist

- [ ] I created and activated a venv at least once.
- [ ] I can explain resource vs endpoint with one real example.
- [ ] I can use `append`, `extend`, `get`, `keys`, and `values` without notes.
- [ ] I completed the JS `fetch` comparison exercise.
- [ ] I completed the Python `main()` wiring drill.
- [ ] I completed the drill and the memorization pass.
