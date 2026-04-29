# Current Week

## Week: 1 — COMPLETE ✅
## Focus: JavaScript Foundations + Shell / Terminal / Environment
## Status: Completed 2026-04-04

## Content Blocks

### Block A: Environment Basics (completed — session 1, ~15 min)
- [x] Terminal vs shell, absolute vs relative paths
- [x] Environment variables and PATH

### Block B: JS Core (completed — session 1, ~15 min)
- [x] Variables, data types, `let`/`const` — verified
- [x] Type coercion — `+` concatenates with strings, `-` converts to number
- [x] `if`/`else`, ternary — `condition ? a : b`
- [x] `switch` — aware, knows fall-through bug
- [x] `for`, `while`, `for...of` — knows for...of, taught distinction

### Block C: Arrays + Array Methods (completed)
- [x] `.filter()`, `.map()`, combined chains — independent mastery
- [x] `.find()`, `.reduce()` (sum, count, max, group-by, dedup, lookup)
- [x] `.some()`, `.every()` — decision tools vs data tools
- [x] Method-combining drill Q1–Q10 completed
- [x] Applied exercise 02: Order Summary Generator

### Block D: Objects + JSON (completed)
- [x] Dot/bracket notation, nested access
- [x] Object vs JSON distinction, JSON.parse/stringify
- [x] Destructuring: basic, alias, default, nested, in array callbacks
- [x] Spread operator for object copy + override
- [x] `?.` optional chaining, `??` nullish coalescing
- [x] Objects + JSON 10-question drill

### Block E: Applied Coding (completed)
- [x] Exercise 01: lead normalizer
- [x] Exercise 02: Order Summary Generator
- [x] Exercise 03: Lead Pipeline capstone (9.5/10)
- [x] `fs` module, `require()`, `Math.round()`

### Block F: Practice Block (completed — session 5, 2026-04-04)
- [x] Part 1: Timed Warm-up (W1–W5) — 5/5 after revision, ~15 min
- [x] Part 2: Pipeline Drills (P1–P5) — 5/5 after revision
- [x] Part 3: File I/O Challenge (F1) — clean after spec fix (`grade` field)
- [x] Part 4: Memorization Pass (M1–M8) — all passed, most needed hints
- [x] Part 5: Speed Round (S1–S10) — 8/10 (S7 spread override blank, S9 `?.` + `??` wrong)

## Completed work (session 5 — 2026-04-04, Week 1 finale)
- `question-bank/week-01/week-01-practice-block.md` — full 5-part practice block completed
- `exercises/week-01/practice-f1.js` — read/filter/transform/write pipeline
- `exercises/week-01/practice-f1-output.json` — generated output
- Week 1 officially closed

## Session 5 mastery diagnosis
**Strengths (recognition-level fluent):**
- All array methods: filter/map/reduce/find/some/every — fluent
- Basic destructuring, spread, ternary chains — fluent
- File I/O full flow (RPTSW: Read-Parse-Transform-Stringify-Write) — canonical shape internalized

**Weak spots (recall-level, needs reinforcement via cross-language use in Week 2+):**
1. `return acc` in `{}` reduce body — still occasionally forgotten
2. `fs.` prefix on read/write — dropped under memory pressure
3. Destructuring alias `:` vs default `=` — needed 2 retries on M6
4. Spread override in inline context (S7) vs named variable (M7) — recognition gap
5. `?.` always returns `undefined` on short-circuit (not original null) — concept gap on S9
6. Arrow function object literal return needs `()` wrapper — tripped twice in same session (P2 + P5)

**Not blocking Week 2** — these will solidify via repeated use in Python contexts and later JS review passes.

## Key concepts learned (Week 1 total)
- Array methods: filter/map/reduce/find/some/every + chaining
- Truthy/falsy, `||` fallback, `(acc[key] || 0) + value` accumulator pattern
- Reduce baton model; reduce find-max no-initial-value shape
- Object access: dot/bracket/nested
- Destructuring: basic, alias (`:`), default (`=`), nested, in callbacks
- Spread `{...obj, key: val}` copy + override
- `?.` optional chaining, `??` nullish coalescing
- JSON parse/stringify, `JSON.stringify(data, null, 2)` pretty-print
- `fs.readFileSync(path, "utf-8")`, `fs.writeFileSync(path, string)`
- `require()`, Node.js module system
- Template literals with `${}`
- Arrow function object return: `=> ({...})`
- Ternary chain for categorization
- Terminal vs shell, Node.js = JS runtime outside browser

## Recurring mistakes to watch (carry into Week 2 reviews)
- `return` missing in `{}` arrow bodies
- `=` vs `===` in conditions
- `fs.` prefix on module methods
- `:` (alias) vs `=` (default) in destructuring
- Arrow function returning object literal without `()` wrapper
- Variable name typos (e.g., `request` vs `requests`, `category` as standalone)
- `JSON.parse` on single string vs array of strings

## Deliverables
- [x] `exercises/week-01/exercise-01.md`
- [x] `exercises/week-01/exercise-02.js`
- [x] `exercises/week-01/exercise-03.js`
- [x] `exercises/week-01/lead-output.json`
- [x] `exercises/week-01/practice-f1.js`
- [x] `exercises/week-01/practice-f1-output.json`
- [x] `question-bank/week-01/week-01-practice-block.md` (full answers inline)
- [ ] `feedback/week-01/` review notes (optional, not blocking)

## Mastery check (final)
- [x] Can use filter/map/reduce/find/some/every without reference
- [x] Can use `.reduce()` for sum, group-by, find-max
- [x] Understands truthy/falsy, `||` fallback
- [x] Can read error messages (ENOENT, TypeError, SyntaxError)
- [x] Can write complete data pipeline independently in new scenario
- [x] Can read/write JSON files with fs module
- [x] Understands destructuring: basic, alias, default, nested, in callbacks
- [x] Understands spread object copy + override
- [x] Understands `?.` and `??` at recognition level
- [~] From-memory recall of patterns — intermediate, will strengthen via Week 2+ cross-language reuse

---

# Week 2 — PREP

## Week: 2
## Focus: HTTP, REST, APIs + Python as Primary Language
## Status: Completed 2026-04-29 — Week 2 closeout pushed
## Environment confirmed: Python 3.12.2 installed ✓

## Why Python now
Per curriculum pivot (2026-03-31), Python becomes primary automation + AI language from Week 2 onwards. JavaScript remains reference/comparison anchor — Week 1 JS foundation means most Python patterns will map 1:1 from known JS patterns.

## Planned Content Blocks (aligned with master-roadmap.md Week 2)

### Block A: HTTP Fundamentals (completed — session 6)
- [x] HTTP methods: GET, POST, PUT, PATCH, DELETE — when to use each
- [x] Status codes: 2xx success, 4xx client error, 5xx server error
- [x] Headers: Content-Type, Authorization, Accept
- [x] Request body vs query parameters

### Block B: Python Environment + Core (completed — session 6 + session 7)
- [x] Verify Python 3.12.2 + pip 24.0 ✓
- [x] `venv` setup — hands-on completed in Session 13
- [x] Running a `.py` file from terminal
- [x] Variables, dynamic typing (no `let`/`const`)
- [x] Data types: `int`, `float`, `str`, `bool`, `None` (vs `null`/`undefined`)
- [x] String methods: `.strip()`, `.lower()`, `.upper()`, `.title()`, f-strings
- [x] `if`/`elif`/`else` — indentation-based
- [x] `for`, `while`, `range()`
- [x] Conditional expression: `a if cond else b`
- [x] `def`, default args, `return`
- [~] `*args`/`**kwargs` intro — light recognition closeout in Session 15, not yet drilled deeply
- [x] `lambda` — anonymous function, `lambda x: expr`, used as `key=` in `sorted()`
- [x] `import` / `from ... import ...` — conceptual, hands-on in Block D
- [x] `if __name__ == "__main__":` idiom

### Block C: Python Collections + Data Manipulation (~60 min, core block)
- [x] `list` (vs JS array): indexing, slicing, `.append()`, `.extend()` — Session 13 gap-closing drill
- [x] `dict` (vs JS object): `dict[key]`, `.items()`, group-by accumulation pattern — Session 8
- [x] `dict` remaining: `.get()`, `.keys()`, `.values()` — Session 13 gap-closing drill
- [~] `tuple` — immutable (new concept, introduced lightly in Session 13; not yet drilled deeply)
- [x] `set` — encountered via `set()` dedup in drill Q9 + `{}` creates set vs value distinction
- [x] **List comprehensions** — mastered (session 7)
  - `[expr for item in iterable]` → map ✓
  - `[expr for item in iterable if cond]` → filter + map ✓
  - ternary in expression: `[A if cond else B for item in iterable]` ✓
  - nested field access: `item["outer"]["inner"]` ✓
- [x] **Dict comprehensions** — mastered (session 8)
  - `{k: v for item in list}` ✓
  - `{k: v for k, v in dict.items()}` ✓
  - filter with `if`: `{k: v for k, v in d.items() if condition}` ✓
- [x] `sum()`, `min()`, `max()`, `len()` built-ins — Session 9
- [x] `sorted()` with `key=` lambda — taught in Session 7
- [x] File I/O: `with open(path) as f:` context manager — Session 9
- [x] `json.load()` / `json.dump()` — Python JSON module — Session 9
- [x] Error handling: `try / except / finally` — Session 10
- [~] Classes basics (enough to read LangGraph framework code later) — light recognition closeout in Session 15

### Block D: REST + API Calls in Python (~45 min)
- [x] REST conventions: resources, endpoints, CRUD mapping — Session 13
- [x] Python `requests` library — install + basic usage
- [x] `requests.get()`, `.post()`, parsing `.json()` response — POST shape added in Session 15
- [x] Handling non-200 status codes, timeouts — Sessions 10-11, reinforced in Session 13
- [x] JS comparison: `fetch()` side-by-side (lightweight, just for mapping) — Session 13

### Block E: Drills (10 questions each, 5 basic + 5 variant)
- [x] HTTP methods + status codes drill — covered in `question-bank/week-02/api-basics-drill-01.md` (session 10)
- [x] Python list comp drill — `question-bank/week-02/listcomp-drill-01.md` (10/10, session 7)
- [x] Python dict comp drill — `question-bank/week-02/dictcomp-drill-01.md` (10/10, session 8)
- [x] Python file I/O + json + built-ins drill — `question-bank/week-02/fileio-drill-01.md` (10/10, session 9)
- [x] Python error handling drill — `question-bank/week-02/error-handling-drill-01.md` (10/10, session 10)
- [x] Python API parsing + error handling drill — `question-bank/week-02/api-basics-drill-01.md` (10/10, session 10)

### Block F: Applied Coding
- [x] Python re-implementation of Week 1 Exercise 03 (lead pipeline) — side-by-side JS comparison — Session 12
- [x] Main exercise: Call a real public API → parse → validate → handle non-200 → filter/transform → save to file (portfolio-ready quality) — `exercises/week-02/session-11-api-summary.py` (session 11)
- [x] Lightweight JS fetch exercise (just to reinforce HTTP concepts in familiar language) — `exercises/week-02/session-13-js-fetch.js`

### Block G: Practice Block (~2 hours, end of week)
- [x] Mixed Python drills: list comps, dict grouping, file I/O — Session 14
- [x] API debugging exercises (given broken requests, find the bug) — Session 14
- [x] Timed coding challenges — Session 14
- [x] Memorization pass + speed round (same 5-part structure as Week 1) — Session 14

## Week 2 Mastery Targets
- [~] Explain GET/POST/PUT/PATCH/DELETE with real examples — GET/POST/DELETE clear, PUT/PATCH still lighter
- [x] Read 401/403/404/429 status codes and explain cause
- [x] Can write list comprehension for filter+map in one line
- [x] Can use dict for group-by patterns
- [x] Can read/write JSON file with `json` module
- [x] Can construct API request with correct headers and body in Python
- [~] Python script handles: missing keys, non-200 status, file write errors — strong in drills; POST network-failure handling not fully implemented
- [x] Can translate JS array methods to Python equivalents (filter→list comp, etc.)
- [x] Can reimplement Week 1 Exercise 03 in Python independently
- [x] **GitHub portfolio: push Week 1 + Week 2 deliverables with README** (pushed 2026-04-29)

## Peripheral exposure for Week 2 (seen, not tested)
- Type hints: `def foo(x: int) -> str:`
- `enumerate()`, `zip()`
- f-string formatting: `f"{value:.2f}"`
- Walrus operator `:=` (rarely, once)
- `requests.Session()` for connection reuse

## Real-world engineering habits (Week 2 = moderate level per CLAUDE.md)
- Dirty data handling becomes normal, not surprise
- "What if this input is null?" asked in reviews
- Helper function suggestion starts appearing
- Naming: snake_case is Python convention (vs camelCase in JS)

## Pacing note (given Week 1 took 5 sessions)
Week 2 is dense (HTTP + full Python + API calls). Realistic split:
- **Session 6:** Block A (HTTP) + Block B (Python env + core syntax)
- **Session 7:** Block B finish + Block C start (list comprehensions)
- **Session 8:** Block C continue (dict methods, dict comprehensions, group-by)
- **Session 9:** Block C continue (built-ins, file I/O, json module)
- **Session 10:** Block C finish + Block D start (error handling + first `requests` flow)
- **Session 11+:** API parsing drill, applied API script, then Week 2 practice block + close

If pace is faster, collapse sessions; if slower, extend. Do not skip Block C depth — list comprehensions are the foundation for everything Python-data-related later.

## Completed work (session 7 — 2026-04-08)
- Block B remainder: `lambda`, `import`, `if __name__ == "__main__"` — all taught
- Block C: list comprehensions — mastered independently
  - filter, map, ternary expression, nested dict access, `sorted()` with `key=lambda`
  - `set()` vs method, `sorted()` vs `.sort()` distinction
  - filter `if` vs ternary `if...else` — key confusion resolved
- `exercises/week-02/session-07-listcomp.py` — filter + transform pipeline, correct output
- `question-bank/week-02/listcomp-drill-01.md` — 10-question drill completed

### Session 7 mastery diagnosis
**What clicked:**
- List comprehension syntax — independent after 2 corrections on first attempt
- Ternary in expression vs filter `if` — confused initially, now clear
- Nested dict access `item["outer"]["inner"]` — correct on second try
- Methods vs functions distinction (`.strip()` vs `set()`) — understood
- `sorted()` with `key=lambda` — understood after natural language translation

**Recurring Python mistakes (watch for Session 8+):**
- Dict uses `:` not `=` — typed `=` multiple times
- Putting `{}` around values accidentally (creates a set, not a value)
- Putting quotes around variable names: `"lead"["score"]` instead of `lead["score"]`
- Wrong bracket placement: `cus["total" > 100]` instead of `cus["total"] > 100`
- Variable name typos under pressure (`eamil`, `customer` instead of `orders`)

**Concept gaps to revisit:**
- `*args`/`**kwargs` — not covered yet, deferred to Session 8
- `dict` formal methods (`.get()`, `.items()`, etc.) — used but not taught
- `list` formal methods (`.append()`, slicing) — not taught yet

## Completed work (session 6 — 2026-04-06)
- Block A: HTTP fundamentals taught (methods, status codes, headers, 401 vs 403 distinction)
- Block B (partial): Python core syntax — variables, types, if/elif/else, for/while, ternary, def/return, f-strings
- `question-bank/week-02/python-basics-drill.md` — 10-question drill completed (9/10 after 3 rounds)
- `exercises/week-02/session-06-warmup.py` — first Python script (JS translation), runs correctly
- `plan/js-to-python-map.md` — JS→Python cheatsheet created
- Key insight: student finds Python more natural than JS (prior Python class exposure)

### Session 6 mastery diagnosis
**What clicked:**
- `def` + indented body + `return` — correct after one correction
- f-string syntax `f"..."` — correct after one correction
- `while` loop 3-part structure (init + condition + increment) — correct after explanation
- `not value` for falsy check — absorbed immediately
- `None` vs `"None"` — understood with analogy

**Still needs work (carry into Session 7):**
- `==` vs `=` in conditions — physically types `=` by default, needed 3 rounds to catch all instances
- Reading task requirements carefully (missed "write a function" and "returns" in Q2)
- f-string nested quotes (outer `"` → inner `'` for dict keys)

## Completed work (session 8 — 2026-04-09)
- Dict methods: `.items()` taught + drilled
- Dict comprehensions: mastered — `{k: v for ...}`, filter, iterate list vs dict
- Group-by accumulation pattern: `for loop + if not in + .append()` — mastered
- `exercises/week-02/session-08-dictcomp.py` — 3 tasks, all correct
- `question-bank/week-02/dictcomp-drill-01.md` — 10/10 completed
- `question-bank/week-02/listcomp-memorization.md` — 8/8 completed (Session 7 backfill)
- `question-bank/week-02/blockb-mini-drill.md` — 8/8 completed (Session 7 backfill)
- `plan/python-block-b-reference.md` — reference doc created

### Session 8 recurring mistakes
- `{}` around values accidentally (creates set not value) — appeared repeatedly
- Variable name vs string literal: `by_region["region"]` vs `by_region[region]`
- filter `if` vs ternary `if...else` position confusion — clarified with "mapping vs sorting hat" analogy
- Dict comprehension written as multi-line for loop (Q6, Q7)
- Group-by attempted as dict comprehension (Q9) — must use for loop pattern
- `key, value:` in dict comp expression slot (confused unpack with new key)
- Lambda: `items` vs `item` typo inside body
- `.lowercased` vs `.lower()` — JS/Swift muscle memory
- `JSON.parse` muscle memory → should be `json.loads` in Python
- `=` vs `==` still appears under memory pressure

### Session 8 concept insights captured
- filter `if` (at end, no else) decides item IN/OUT
- ternary `if...else` (at start, has else) decides item VALUE
- Group-by: "needs to accumulate into same key → for loop, one new entry per iteration → comprehension"
- Lambda anatomy: same name on both sides of `:`
- `import X` vs `from X import Y` — prefix vs no-prefix tradeoff
- `__name__ == "__main__"` = "only run when I'm the main character"

## Completed work (session 9 — 2026-04-12)
- Warm-up: group-by reinforcement (transactions → user-total) — completed with 2 correction rounds
- Built-ins: `sum()`, `len()`, `min()`, `max()`, `round()` — taught and used in exercise
- File I/O: `with open(path, mode) as f:` context manager — concept of "remote control vs content" clicked
- Mode distinction: `"r"` (read, must exist) vs `"w"` (write, creates/overwrites) vs `"a"` (append)
- `json` module: `json.load(f)` vs `json.loads(s)`, `json.dump(data, f)` vs `json.dumps(data)`, `indent=2`
- Relative vs absolute paths, `os.getcwd()`, cwd depends on terminal location not file location
- `exercises/week-02/session-09-fileio.py` — full pipeline: read raw JSON → filter active → clean strings → compute stats → pretty-printed write
- `exercises/week-02/session-09-raw-leads.json` — test input with dirty data (whitespace, uppercase, mixed status)
- `exercises/week-02/session-09-clean-leads.json` — generated output (6 leads + stats)
- `question-bank/week-02/fileio-drill-01.md` — 10/10 completed (multiple correction rounds)
- `question-bank/week-02/fileio-memorization.md` — generated, deferred to Session 10 start

### Session 9 mastery diagnosis
**What clicked:**
- `with open()` context manager + why auto-close matters
- `r` vs `w` vs `a` mode distinction
- `json.load(f)` vs `f.read()` — parsed vs raw string
- File path resolution relative to cwd (not script location)
- Full pipeline: read → filter → transform → stats → write — independent after tasks 1-2

**Recurring mistakes (tracked — happening across multiple sessions):**
1. **Literal-string trap in comprehension expression slot** — wrote `"price"` instead of `product["price"]`, `"paid"` instead of `paid` (variable). Occurred 4+ times in Q6, Q9, Q10.
2. **Dict uses `:` not `=`** — still wrote `"count" = len(...)` in drill Q9
3. **`f` is remote control, not content** — wrote `text = f` (skipped `.read()`) three times in Q1-Q3
4. **Missing `.json` file extension** in open() calls (twice in Q10)
5. **Missing `:` after `with open(...) as f`** (once in Q10)
6. **Function call vs indexing**: wrote `max[score]` instead of `max(score)` in exercise
7. **Group-by attempted with dict comprehension again** (Q10 Step C) — same mistake as Session 8, still needs reinforcement: accumulation requires for loop
8. **Path prefix `/`** added to relative path causing FileNotFoundError (`/exercises/...` → tried root of disk)

### Session 9 concept insights captured
- `with` = "用完自动收尾" (auto-cleanup), not about opening per se
- `open()` returns a "file handle" (remote control), nothing read yet
- Mode `"w"` silently wipes existing content — dangerous if used by mistake
- Keyword arguments require `=` (e.g., `indent=2`), not space-separated
- Variable name vs string literal distinction applies everywhere: comprehensions, dict values, function args
- JSON file content is always a string until parsed — `f.read()` gives string, `json.load()` gives dict/list

## Next session agenda (Session 10 — Block C finish + Block D start)
1. **Memorization pass** (deferred from Session 9): `fileio-memorization.md` — 8 questions, canonical shapes
2. Review recurring mistakes (esp. literal-string trap + group-by loop vs comprehension)
3. Error handling: `try / except / finally` basics
4. `*args`/`**kwargs` — quick intro (deferred from Session 7+8, time-boxed)
5. Block D start: first `requests` GET request + status check + `.json()` parsing
6. Applied: fetch a real public API, transform fields, write a small JSON output

### Peripheral exposure for Session 10 (weave in, don't test directly)
- `os.path.join()` for portable paths (introduced conceptually in Session 9 but not drilled)
- `os.getcwd()` / `os.path.dirname(__file__)` for script-relative paths
- Filter `if` vs ternary `if...else` distinction — keep reinforcing
- Group-by for loop pattern — keep reinforcing until fluent

### Session 10 prep status (2026-04-13)
- `question-bank/week-02/fileio-memorization.md` ready as the opening recall gate
- `question-bank/week-02/error-handling-drill-01.md` generated
- `question-bank/week-02/api-basics-drill-01.md` generated
- `exercises/week-02/session-10-api-intro.py` starter exercise generated
- `feedback/week-02/teacher-handoff.md` added to preserve learning profile and teaching approach
- Environment check: `requests` available (`2.32.5`)

### Session 10 progress so far (2026-04-13)
- Opening recall gate completed: `question-bank/week-02/fileio-memorization.md`
- File I/O canonical shapes now recalled correctly after revision:
  - plain text read -> `f.read()`
  - plain text write -> `f.write(...)`
  - JSON read -> `json.load(f)`
  - JSON write -> `json.dump(data, f, indent=2)`
- Student can now state the core distinction:
  - `f` is a file handle / open-file connection, not the file content
  - `json.load(f)` returns a parsed Python object (`dict` / `list`), not a raw string
- Group-by accumulation pattern recalled correctly after correction rounds
- Error handling drill completed: `question-bank/week-02/error-handling-drill-01.md`
- Student can now distinguish:
  - predictable branch -> `if`
  - runtime failure risk -> `try / except`
  - always-run cleanup / final step -> `finally`
- Common exception types now recognized by scenario:
  - bad numeric conversion -> `ValueError`
  - divide by zero -> `ZeroDivisionError`
  - missing file -> `FileNotFoundError`
  - invalid JSON -> `json.JSONDecodeError`

### Session 10 recurring mistakes observed in memorization
1. Plain text vs JSON operations mixed at first (`f.read` / `f.write` vs `json.load` / `json.dump`)
2. File path string vs content string confusion in write tasks
3. Variable name vs string literal confusion (`data` vs `"data"`)
4. Group-by membership check initially targeted the value instead of the key
5. Comprehension variable mismatch under pressure (`fil` vs `f`)

### Session 10 recurring mistakes observed in error handling drill
1. Began by treating `try` / `except` / `finally` like inline syntax instead of block syntax
2. Needed reinforcement that `except` catches an exception type, not an error message string
3. Sometimes placed `try` too deep, missing failures from `open(...)`
4. Success-path return / print omitted once the exception path was in place
5. Spec-reading precision still matters (`users.json` vs `user.json`)

### Session 10 progress in API basics (2026-04-16)
- API basics drill completed: `question-bank/week-02/api-basics-drill-01.md`
- Student can now use:
  - `requests.get(...)`
  - `response.status_code`
  - `response.json()`
  - `params={...}` for query parameters
  - `headers={...}` for request metadata
  - `timeout=10` as a request option (not a query param)
  - `requests.RequestException` for request-level failures
- Student can now explain the distinction:
  - `params` = which data the caller wants
  - `headers` = how the request should be handled / identity / accepted format
  - `response` = HTTP response object, not parsed JSON yet
  - `response.json()` = parsed Python data from the response body
- `exercises/week-02/session-10-api-intro.py` cleaned into a single final flow after refactor review

### Session 10 recurring mistakes observed in API basics drill
1. JS muscle memory initially appeared again (`JSON.parse`, `request.get`, `=` vs `==`)
2. Dict syntax inside `params={...}` still needed one correction (`:` vs `=`)
3. Request options vs query params needed clarification (`timeout=10` vs `params={...}`)
4. Success-path return placement still needed one indentation correction in `fetch_user_names()`
5. Student benefits from story-mode explanation when the request/response lifecycle is involved

### Teaching preference update (2026-04-16)
- Student wants repo-level Claude teaching rules treated as active operating rules for all tutors/agents, not just Claude.
- Mixed CN/EN chat style must follow the repo guidance more strictly:
  - preserve English logic
  - keep technical/workflow vocabulary in English
  - use Chinese mainly for connectors, helper words, and readability
- Student prefers story-mode concept teaching for new material:
  1. the engineer's task
  2. the reasoning path
  3. local vs remote/system interaction
  4. likely failure points
  5. why the new concept/pattern solves the problem
- Repo files remain English-only; this preference applies to direct chat teaching only.

### Immediate next step for Session 10
1. Start Block F applied coding with `exercises/week-02/session-11-api-summary.py`
2. Reuse the same request lifecycle:
   - `requests.get(...)`
   - `params={...}`
   - `response.status_code`
   - `response.json()`
   - filter / transform / write output
3. Keep the same low-hint + story-mode teaching pattern through the applied script

### Session 11 progress in applied coding (2026-04-18)
- Applied API summary script completed: `exercises/week-02/session-11-api-summary.py`
- Student used the full request lifecycle in one script:
  - `requests.get(...)`
  - `params={"userId": USER_ID}`
  - `timeout=10`
  - `response.status_code`
  - `response.json()`
  - filter completed items
  - build summary output
  - `json.dump(...)` to file
- Script was cleaned into a single final flow after exercise completion.

### Session 11 recurring mistakes observed in applied coding
1. API parameter names and option names still need exact recall (`params`, `userId`)
2. Variable vs string-literal confusion can still appear under pressure (`OUTPUT_PATH`, `output`)
3. Student benefits from reusing previously built intermediate data instead of refiltering from raw input
4. Recall gaps are now more common than concept gaps in request/response work

### Immediate next step after Session 11
1. Do the remaining Week 2 applied piece: Python re-implementation of Week 1 Exercise 03
2. Then run the Week 2 practice block / closeout
3. After that, clean and push Week 2 deliverables with README

### Session 12 prep status (2026-04-18)
- Starter generated: `exercises/week-02/session-12-lead-pipeline.py`
- This task reuses the Week 1 capstone input:
  - `exercises/week-01/raw-leads.json`
- Main teaching goal:
  - translate the same business pipeline from JavaScript thinking into Python thinking
  - keep named functions and file I/O
  - reuse list filtering, transformation, group-by counting, and summary building

### Session 12 progress in Python pipeline translation (2026-04-18)
- Python lead pipeline completed: `exercises/week-02/session-12-lead-pipeline.py`
- Output generated: `exercises/week-02/session-12-lead-output.json`
- Student successfully translated the Week 1 JS capstone into Python with:
  - `json.load(...)`
  - function-by-function filtering and transformation
  - summary building with loop + accumulator pattern
  - `main()` orchestration
  - `json.dump(...)` output

### Session 12 recurring mistakes observed
1. File I/O shape was briefly mixed with API-response habits (`response.json()` vs `json.load(f)`)
2. Local variable scope across helper functions still needed reinforcement (`return` + parameter flow)
3. Relative path behavior differed between Interactive Window and terminal execution
4. Aggregation logic initially mixed single-item thinking with whole-list thinking in `summarize_leads()`
5. Parameter names vs outer constants (`path` vs `INPUT_PATH`) still affect readability for the student

### Session 12 concept insights captured
- `main()` is the script orchestrator, not a magic place that can see every local variable
- Function-to-function data flow should be read as: input -> helper -> returned output -> next helper
- The parameter name inside a function is local to that function, even if the caller passes a global constant
- Terminal output and file output are different checkpoints; `print(summary)` is not the same as the final saved JSON

### Immediate next step after Session 12
1. Run Session 13 gap-closing work before the Week 2 practice block
2. Cover the remaining hands-on gaps:
   - `venv` workflow
   - REST resource/endpoint mapping
   - Python list/dict basics still marked as deferred
   - lightweight JS `fetch` comparison
3. Add one explicit `main()` wiring drill so orchestration is practiced directly, not only implicitly

### Session 13 prep status (2026-04-18)
- Session guide created: `exercises/week-02/session-13-gap-closing.md`
- Gap-closing drill created: `question-bank/week-02/rest-collections-drill-01.md`
- Memorization pass created: `question-bank/week-02/session-13-main-memorization.md`
- JS comparison starter created: `exercises/week-02/session-13-js-fetch.js`
- Python `main()` starter created: `exercises/week-02/session-13-main-wiring.py`
- Input data created for the wiring drill: `exercises/week-02/session-13-orders.json`

### Session 13 agenda
1. `venv` hands-on mini lab
2. REST conventions quick map: resource vs endpoint vs CRUD
3. Python collections gap closing: indexing, slicing, `append`, `extend`, `get`, `keys`, `values`, tuple concept
4. Lightweight JS `fetch` side-by-side with Python `requests`
5. Explicit `main()` wiring drill
6. Drill + memorization pass before ending the session

### Session 13 progress in gap closing + API mapping (2026-04-20)
- Gap-closing drill completed: `question-bank/week-02/rest-collections-drill-01.md`
- Memorization pass completed: `question-bank/week-02/session-13-main-memorization.md`
- Python orchestration drill completed: `exercises/week-02/session-13-main-wiring.py`
- Output generated: `exercises/week-02/session-13-order-summary.json`
- Lightweight JS `fetch` comparison completed: `exercises/week-02/session-13-js-fetch.js`
- Output generated: `exercises/week-02/session-13-fetch-output.json`
- Student now has recall-level or better command of:
  - `venv` create + activate workflow
  - resource vs endpoint vs CRUD mapping
  - indexing vs slicing, `append` vs `extend`
  - safe dict lookup with `.get()`
  - `keys()` / `values()`
  - `main()` as orchestration layer
  - Python `requests` flow vs JS `fetch` flow

### Session 13 recurring mistakes observed
1. New CS / systems concepts still stall if drills appear before concept framing
2. HTTP method names vs CRUD action words were initially mixed (`PATCH` vs `update`)
3. JS async response parsing still needs reinforcement (`await response.json()`)
4. Terminology alone is not enough; student needs the problem the design is solving before memorizing labels
5. Session materials are more effective when introduced in this order: why -> mental model -> analogy -> tiny example -> drill

### Teaching preference refinement (2026-04-20)
- For new CS / systems topics, explain in this order before drilling:
  1. what engineering problem exists
  2. why the language/tool designers made this feature
  3. how an engineer actually uses it
  4. one plain analogy
  5. one tiny concrete example
- If a drill assumes vocabulary the student has not internalized yet, pause and teach the concept first rather than pushing through the drill

### Immediate next step after Session 13
1. Start Session 14: Week 2 practice block
2. Use the practice block to formally verify mastery targets rather than just concept exposure
3. Keep emphasis on:
   - request/response lifecycle recall
   - group-by and JSON/file I/O fluency
   - `main()` wiring and multi-function organization
   - method vs action-word distinction in REST/API work

### Session 14 prep status (2026-04-27)
- Week 2 practice block created: `question-bank/week-02/week-02-practice-block.md`
- Timed coding challenge starter created: `exercises/week-02/session-14-practice-challenge.py`
- Challenge input created: `exercises/week-02/session-14-raw-tickets.json`

### Session 14 agenda
1. Timed warm-up: list comp, group-by, safe lookup, request lifecycle, `main()` shape
2. API debugging exercises: broken request lines, params vs headers, JSON parsing, JS async parsing
3. Timed coding challenge: file I/O + filtering + normalization + summary + output write
4. Memorization pass: canonical Python/JS/API/file-I/O shapes
5. Speed round: quick recall of slicing, methods, endpoints, venv, and response handling

### Session 14 progress in Week 2 practice block (2026-04-28)
- Practice block completed: `question-bank/week-02/week-02-practice-block.md`
- Timed coding challenge completed: `exercises/week-02/session-14-practice-challenge.py`
- Output generated: `exercises/week-02/session-14-triage-output.json`
- Student completed all 5 practice parts:
  - timed warm-up
  - API debugging
  - timed coding challenge
  - memorization pass
  - speed round
- Final challenge output verified:
  - `ticketCount = 3`
  - `byTeam = {"integrations": 1, "platform": 1, "ops": 1}`
  - `urgentIds = ["T-105"]`

### Session 14 mastery diagnosis
**What held up under pressure:**
- list comprehension filter + map pattern
- group-by accumulation with for loop + `if not in`
- JSON file read/write canonical shapes
- request lifecycle: `requests.get(...)`, `status_code`, `response.json()`
- `main()` wiring and end-to-end script flow
- safe dict lookup with `.get()`
- JS `fetch` recall at recognition level (`await fetch`, `await response.json()`)

**What still needed correction rounds:**
1. `dict.get(...)` vs HTTP `GET` still competes in recall
2. operator precedence in boolean conditions still needs deliberate parentheses when the logic is `A and (B or C) and D`
3. slicing end-exclusive rule (`[1:4]` does not include index `4`) is still not automatic
4. API debugging answers were conceptually closer than before, but explanation quality is still weaker than code correction quality
5. student still benefits from separating:
   - lookup vs assignment
   - request failure vs non-200 status
   - local object method vs HTTP method sharing the same English word

### Immediate next step after Session 14
1. Start Session 15: Week 2 closeout + portfolio prep
2. Clean remaining Week 2 loose ends:
   - lightweight POST exposure
   - `tuple` / classes basics / `*args` + `**kwargs` as light closeout topics
   - README + GitHub push for Week 1 + Week 2 deliverables
3. Use Session 15 to convert current working skill into final Week 2 artifacts and mastery sign-off

### Session 15 prep status (2026-04-28)
- Session guide created: `exercises/week-02/session-15-closeout.md`
- Lightweight POST starter created: `exercises/week-02/session-15-post-intro.py`
- Week 2 closeout check created: `question-bank/week-02/week-02-closeout-check.md`
- Week 2 README created: `exercises/week-02/README.md`

### Session 15 agenda
1. Lightweight POST exposure with `requests.post(...)` and `json=PAYLOAD`
2. Week 2 closeout check: methods, status codes, resource vs endpoint, `dict.get` vs `requests.get`
3. Light recognition closeout: `tuple`, `*args`, `**kwargs`, classes basics
4. README review and portfolio cleanup
5. Git status review and Week 2 sign-off prep

### Session 15 progress in closeout + portfolio prep (2026-04-28)
- Lightweight POST script completed at logic level: `exercises/week-02/session-15-post-intro.py`
- Live POST request could not complete because outbound network was blocked in the environment (`requests.exceptions.ConnectionError` / WinError 10013)
- Week 2 closeout check completed: `question-bank/week-02/week-02-closeout-check.md`
- Week 2 README reviewed and accepted: `exercises/week-02/README.md`
- Git status reviewed; repo is still a heavily dirty worktree, so Week 2 push prep is not yet complete

### Session 15 mastery diagnosis
**What is now solid enough to sign off for Week 2 study goals:**
- GET vs POST at the practical level
- status-code recognition: 401 / 403 / 404 / 429
- resource vs collection endpoint vs single-item endpoint
- `dict.get(...)` vs `requests.get(...)`
- `*args`, `**kwargs`, and class basics at recognition level
- README-level explanation of major Week 2 artifacts

**What remains as final closeout work rather than learning work:**
1. GitHub push for Week 1 + Week 2 deliverables
2. Optional strengthening of PUT/PATCH explanation depth
3. Optional stronger `requests.post(...)` error handling once network access is available

### Immediate next step after Session 15
1. Start Week 3 SQL Deep Dive
2. Keep Week 2 drills available for spaced review as needed
3. Use Week 2 artifacts as reference when SQL work begins to touch files, APIs, and pipelines again
