# Week 1 — Feedback Summary

**Weeks covered:** 2026-03-29 to 2026-04-04
**Sessions:** 5
**Status:** Complete ✅

---

## What the student learned
- JavaScript array methods: filter, map, reduce, find, some, every (chaining + standalone)
- Objects + JSON: dot/bracket access, destructuring (basic/alias/default/nested/in callbacks), spread override
- Optional chaining `?.` and nullish coalescing `??`
- Template literals, ternary chains, arrow function object return `=> ({...})`
- Node.js fs module: `readFileSync`, `writeFileSync`, `JSON.parse`, `JSON.stringify(data, null, 2)`
- Terminal vs shell, environment basics

## Exercises completed
1. `exercises/week-01/exercise-01.md` — lead normalizer
2. `exercises/week-01/exercise-02.js` — order summary generator
3. `exercises/week-01/exercise-03.js` — lead pipeline capstone (9.5/10)
4. `exercises/week-01/practice-f1.js` — practice block file I/O challenge
5. `question-bank/week-01/week-01-practice-block.md` — full 5-part practice (warm-up, pipeline drills, file I/O, memorization, speed round)

## Mastery snapshot
**Recognition level — strong across all topics.**
**Recall level — intermediate**, with specific weak spots to reinforce during Week 2+ via cross-language use:

1. `return acc` missing in `{}` reduce bodies (recurring)
2. `fs.` prefix dropped under memory pressure
3. Destructuring `:` (alias) vs `=` (default) — needs 2+ retries
4. Arrow function returning object literal needs `()` wrapper (tripped twice in one session)
5. Spread override recognized in named-variable form but not in inline-literal form
6. `?.` always returns `undefined` on short-circuit (not original null)
7. Variable name typos (`request` vs `requests`, etc.)
8. `JSON.parse` on single string vs array of strings (context awareness)

## Recurring mistakes to carry forward
- `=` vs `===` in conditions
- `return` missing in `{}` arrow bodies
- Missing module prefixes (`fs.`, `Math.`)
- Object literal return without `()` wrapper
- Spec reading carelessness (field name mismatch: `grade` vs `group`)

## Strengths to build on
- Clean diagnostic reasoning — can identify bugs when pointed to them
- Good use of self-awareness (flags "looked at notes" and "logic gap here" during practice)
- Pace: completed all Block F (5-part practice) in one session
- Asks good conceptual questions (e.g., "why return 0 instead of returning a string?")

## Transition to Week 2
No remedial work needed. Weak spots will strengthen naturally via:
- Python list comprehensions reinforcing filter+map mental model
- Python dict operations reinforcing object/group-by patterns
- Re-implementing Week 1 Exercise 03 in Python (side-by-side comparison)
- Continued practice with JSON I/O in both languages

Move forward to Week 2: HTTP, REST, APIs + Python as primary language.
