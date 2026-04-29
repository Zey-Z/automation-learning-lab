# Session 15 - Week 2 Closeout + Portfolio Prep

**Goal:** close Week 2 cleanly, add one lightweight `POST` exposure, verify mastery targets, and prepare a Week 2 README for portfolio use.

**Deliverables:**
- `exercises/week-02/session-15-post-intro.py`
- `question-bank/week-02/week-02-closeout-check.md`
- `exercises/week-02/README.md`

---

## Part 1 - Lightweight POST exposure (~20 min)

Complete:
- `exercises/week-02/session-15-post-intro.py`

**What this part is for:**
- `GET` = ask the server for data
- `POST` = send new data to the server
- `params={...}` is for query parameters
- `json={...}` is for a JSON request body
- successful create requests often return `201`

Run from repo root:

```powershell
python exercises/week-02/session-15-post-intro.py
```

If network access fails, still complete the code shape and explain what each line is trying to do.

---

## Part 2 - Week 2 closeout check (~20 min)

Complete:
- `question-bank/week-02/week-02-closeout-check.md`

This is not for new concepts. It checks whether the Week 2 ideas are clear enough to explain without relying only on syntax memory.

Focus:
- HTTP methods and status codes
- resource vs endpoint
- `dict.get(...)` vs `requests.get(...)`
- `tuple`, `*args`, `**kwargs`, classes basics at recognition level

---

## Part 3 - README review (~20 min)

Open:
- `exercises/week-02/README.md`

Task:
1. read the descriptions
2. confirm they match what you actually built
3. adjust anything that feels inaccurate or too vague

The main goal is that you can explain:
- what each Week 2 script does
- what input/output it uses
- which patterns you learned

---

## Part 4 - Portfolio cleanup (~20 min)

Before Git work, verify:
- scripts still run
- JSON outputs exist
- filenames are clear
- no placeholder TODO comments remain in final deliverables you want to show

Priority Week 2 artifacts:
- `session-11-api-summary.py`
- `session-12-lead-pipeline.py`
- `session-13-js-fetch.js`
- `session-13-main-wiring.py`
- `session-14-practice-challenge.py`

---

## Part 5 - Git prep (~10 min)

When artifacts are clean, check:

```powershell
git status --short
```

If everything looks right, Session 15 can end with:
- Week 2 mastery sign-off
- README ready
- Git push prep ready

---

## End-of-session checklist

- [ ] I completed the lightweight POST script or can explain its full flow.
- [ ] I completed the Week 2 closeout check.
- [ ] I reviewed the Week 2 README and understand every listed artifact.
- [ ] I can explain GET vs POST with one real example.
- [ ] I can explain `dict.get(...)` vs `requests.get(...)` without mixing them.
- [ ] Week 2 files are clean enough for portfolio review.
