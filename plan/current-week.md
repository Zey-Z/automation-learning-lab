# Current Week

## Week: 1
## Focus: JavaScript Foundations + Shell / Terminal / Environment
## Status: In progress

## Content Blocks

### Block A: Environment Basics (completed — session 1, ~15 min)
- [x] Terminal vs shell, absolute vs relative paths
- [x] Environment variables and PATH

### Block B: JS Core (completed — session 1, ~15 min)
- [x] Variables, data types, `let`/`const` — verified
- [x] Type coercion — taught: `+` concatenates with strings, `-` converts to number
- [x] `if`/`else`, ternary — taught syntax: `condition ? a : b`
- [x] `switch` — aware it exists, knows fall-through bug
- [x] `for`, `while`, `for...of` — knows for...of, taught distinction

### Block C: Arrays + Array Methods (in progress)
- [x] `.filter()` — learned and drilled to independent mastery
- [x] `.map()` — learned and drilled to independent mastery
- [x] `.filter()` + `.map()` combined — independent in new scenario (drill-02, zero bugs)
- [ ] `.find()` — not yet
- [ ] `.reduce()` — not yet
- [ ] `.some()`, `.every()` — not yet
- [ ] 10-question drill for find/reduce/some/every

### Block D: Objects + JSON (not started)
- [ ] Object access, destructuring, spread operator
- [ ] JSON: parse, stringify, nested access, handle missing keys
- [ ] 10-question drill (5 basic + 5 variant)

### Block E: Applied Coding (partially done)
- [x] Exercise 01: lead normalizer — completed
- [ ] Exercise 02: data pipeline (read JSON → validate → transform → write output)
- [ ] New skill: `fs` module (file I/O)

### Block F: Practice Block (~2 hours, not started)
- [ ] Mixed drills across all Block A–D skills
- [ ] Timed exercises
- [ ] Memorization passes
- [ ] New-scenario drills

## Completed work (session 1 — 2026-03-29, 2.5 hours)
- `exercises/week-01/exercise-01.md` — lead normalizer exercise
- `submissions/week-01/exercise-01.js` — lead normalizer solution
- `question-bank/javascript/filter-map-drill-01.md` — 5-question drill (completed)
- `question-bank/javascript/filter-map-drill-02.md` — new scenario drill (completed independently, zero bugs)
- `submissions/week-01/drill-02.js` — drill 02 solution

## Key concepts learned
- `.filter()` — keep items where condition is truthy, returns new array
- `.map()` — transform each item, return new object, returns new array
- `.map()` does NOT mutate original — must assign result with `=`
- truthy/falsy: `""`, `0`, `null`, `undefined`, `false` are falsy
- `.filter()` is for judging, `.map()` is for transforming
- terminal = window, shell = interpreter
- ternary: `condition ? valueIfTrue : valueIfFalse`
- type coercion: `+` concatenates strings, `-` converts to number

## Recurring mistakes to watch
- Using array name instead of item name after `=>` (e.g., `orders.status` instead of `order.status`)
- Strings need quotes in comparisons (`=== "paid"` not `=== paid`)

## Deliverables
- [x] `submissions/week-01/exercise-01.js`
- [ ] `submissions/week-01/exercise-02-data-pipeline.js`
- [ ] `feedback/week-01/` review notes

## Mastery check
- [x] Can use `.filter()`, `.map()` without reference
- [ ] Can use `.find()`, `.reduce()` without reference
- [x] Understands truthy/falsy
- [x] Can read error messages and identify error type
- [x] Can write a complete data cleaning function independently in a new scenario

## Next session
- Block C continued: `.find()`, `.reduce()`, `.some()`, `.every()`
- Block D: Objects + JSON
- Block E: Exercise 02 — data pipeline with `fs` module
