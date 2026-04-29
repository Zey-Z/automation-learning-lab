# Week 2 - HTTP, REST, APIs, and Python

This folder contains the main Week 2 practice artifacts for moving from JavaScript-oriented data work into Python-oriented automation workflows.

## Main skills practiced

- Python script structure with `main()`
- List comprehensions and dict-based grouping
- File I/O with `with open(...)`
- JSON read/write with `json.load(...)` and `json.dump(...)`
- Error handling with `try` / `except`
- HTTP request lifecycle with `requests`
- Basic API comparison between Python `requests` and JavaScript `fetch`

## Key artifacts

### `session-10-api-intro.py`
First Python API script using:
- `requests.get(...)`
- `response.status_code`
- `response.json()`

### `session-11-api-summary.py`
Fetches todo items from a public API, filters completed items, and writes a small JSON summary file.

Run:

```powershell
python exercises/week-02/session-11-api-summary.py
```

### `session-12-lead-pipeline.py`
Python reimplementation of the Week 1 JavaScript lead pipeline.

Input:
- `exercises/week-01/raw-leads.json`

Output:
- `exercises/week-02/session-12-lead-output.json`

Run:

```powershell
python exercises/week-02/session-12-lead-pipeline.py
```

### `session-13-main-wiring.py`
Focused practice on `main()` orchestration and helper-function data flow.

### `session-13-js-fetch.js`
Lightweight JavaScript comparison exercise for:
- `fetch(...)`
- `await response.json()`
- query params in the URL

Run:

```powershell
node exercises/week-02/session-13-js-fetch.js
```

### `session-14-practice-challenge.py`
Week 2 practice-block coding challenge covering:
- file I/O
- filtering
- normalization
- group-by summary logic
- `main()` orchestration

Input:
- `exercises/week-02/session-14-raw-tickets.json`

Output:
- `exercises/week-02/session-14-triage-output.json`

Run:

```powershell
python exercises/week-02/session-14-practice-challenge.py
```

## Supporting practice files

- `session-06-warmup.py`
- `session-07-listcomp.py`
- `session-08-dictcomp.py`
- `session-09-fileio.py`
- `session-13-gap-closing.md`
- `session-15-post-intro.py`

## Week 2 outcome

By the end of Week 2, the main goal is to be able to:

- read and write JSON files in Python
- filter and transform business data with Python collections
- explain the request/response lifecycle
- make and debug simple API calls
- organize a small automation script into helper functions plus `main()`
