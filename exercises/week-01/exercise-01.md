# Exercise 01 — Clean Lead Data

## Skill target
Use `.filter()`, `.map()`, string methods (`.trim()`, `.toLowerCase()`), and basic validation.

## Scenario
You received raw lead data from a webhook. Clean it before saving to a CRM.

## Input
```js
const leads = [
  { name: "  Alice ", email: "  ALICE@EXAMPLE.COM ", source: "webinar" },
  { name: "Bob", email: "", source: "referral" },
  { name: " Charlie", email: "charlie@test.com  ", source: "ads" },
  { name: "", email: "dave@example.com", source: "webinar" },
  { name: "Eve", email: "   EVE@SAMPLE.COM", source: "" },
  { name: " Frank ", email: "frank@test.com", source: "referral" },
]
```

## Requirements
1. **Reject** any lead that has an empty `name` OR empty `email` (after trimming)
2. **Clean** the remaining leads:
   - trim whitespace from `name`, `email`, and `source`
   - lowercase the `email`
3. Return an object: `{ cleaned: [...], rejected: [...] }`
   - `cleaned` = array of cleaned lead objects
   - `rejected` = array of the original (uncleaned) lead objects that failed validation

## Constraints
- Use `.filter()` or `.map()` — do not use `for` loops
- No external libraries

## Expected output shape
```js
{
  cleaned: [
    { name: "Alice", email: "alice@example.com", source: "webinar" },
    // ... more
  ],
  rejected: [
    { name: "Bob", email: "", source: "referral" },
    // ... more
  ]
}
```

## Rubric
- correctness: does it produce the right cleaned/rejected split?
- clarity: is the code readable?
- robustness: does it handle edge cases (whitespace-only strings)?
- reasoning: can you explain why you used filter/map?
