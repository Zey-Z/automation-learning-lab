# Week 1 Practice Block — Mixed Drills

Estimated time: ~2 hours
Goal: fluency across all Week 1 skills. No new concepts — pure repetition and speed.

---

## Part 1: Timed Warm-up (20 min)

Set a timer. Try to finish all 5 without looking at notes.

### W1 — filter + map
```js
const tasks = [
  { title: "Deploy API", priority: "high", done: false },
  { title: "Fix typo", priority: "low", done: true },
  { title: "Write tests", priority: "high", done: false },
  { title: "Update docs", priority: "medium", done: false },
  { title: "Code review", priority: "high", done: true },
];

tasks.filter(t => t.done ===false && t.priority === "high").map(t=> t.title)

```
Get an array of titles of **undone high-priority** tasks.
Expected: `["Deploy API", "Write tests"]`

---

### W2 — reduce group-by
```js
const logs = [
  { action: "login", user: "alice" },
  { action: "purchase", user: "bob" },
  { action: "login", user: "carol" },
  { action: "login", user: "alice" },
  { action: "purchase", user: "alice" },
];

logs.reduce((acc,l)=>{
  acc[l.action] = acc[l.action] || []
  acc[l.action].push(l.user)
  return acc
},{})

```
Group user names by action. Expected:
```js
{ login: ["alice", "carol", "alice"], purchase: ["bob", "alice"] }
```

---

### W3 — reduce find-max
```js
const products = [
  { name: "Laptop", revenue: 45000 },
  { name: "Phone", revenue: 72000 },
  { name: "Tablet", revenue: 31000 },
  { name: "Monitor", revenue: 58000 },
];

products.reduce((acc,p)=>{
  return acc.revenue > p.revenue ? acc:p 
}).name

```
Find the product name with the highest revenue. Expected: `"Phone"`

---

### W4 — some + every
```js
const invoices = [
  { id: "INV-01", amount: 500, paid: true },
  { id: "INV-02", amount: 0, paid: true },
  { id: "INV-03", amount: 300, paid: false },
  { id: "INV-04", amount: 150, paid: true },
];

invoices.some(i => i.paid === false) //return true
invoices.every(i => i.amount > 0) //return false


```
1. Are there any unpaid invoices? (use `.some()`)
2. Do all invoices have `amount > 0`? (use `.every()`)

---

### W5 — destructuring + template literal
```js
const order = {
  orderId: "ORD-500",
  customer: { name: "Dan Lee", email: "dan@test.com" },
  total: 249.99
};

const {orderId, customer: {name}, total} = order
const message = `order ${orderId} for ${name} — $${total}` 


```
Destructure to get `orderId`, `name` (from customer), and `total`. Then create a string:
`"Order ORD-500 for Dan Lee — $249.99"`

---

## Part 2: Pipeline Drills (30 min)

Each drill requires chaining 2-3 methods. Write and run each one.

### P1 — filter + reduce: Total unpaid amount
```js
const bills = [
  { vendor: "AWS", amount: 1200, paid: false },
  { vendor: "Slack", amount: 50, paid: true },
  { vendor: "GitHub", amount: 100, paid: false },
  { vendor: "Figma", amount: 75, paid: true },
  { vendor: "AWS", amount: 800, paid: false },
];

bills.filter(b => b.paid === false).reduce((acc,b) => {
  acc = acc + b.amount
  return acc
}, 0)
```
Filter unpaid bills, then reduce to total amount. Expected: `2100`

---

### P2 — filter + map + spread: Enrich active users
```js
const users = [
  { id: 1, name: "Alice", active: true, plan: "pro" },
  { id: 2, name: "Bob", active: false, plan: "free" },
  { id: 3, name: "Carol", active: true, plan: "free" },
  { id: 4, name: "Dan", active: true, plan: "pro" },
];

users.filter(u => u.active === true).map(u => ({
  ...u,
  badge: "verified"
}))
```
Filter active users, then map to new objects with all original fields plus `badge: "verified"`. Expected first item:
```js
{ id: 1, name: "Alice", active: true, plan: "pro", badge: "verified" }
```

---

### P3 — map + reduce: Average response time
```js
const requests = [
  { url: "/api/users", ms: 120 },
  { url: "/api/orders", ms: 340 },
  { url: "/api/health", ms: 15 },
  { url: "/api/products", ms: 200 },
  { url: "/api/auth", ms: 89 },
];

const total = requests.map(r => r.ms).reduce((acc,r) => {
  acc = acc + r
  return acc
}, 0)

const ave = Math.round(total / requests.length)

```
Map to extract just the `ms` values, then reduce to calculate the average (use `Math.round`). Expected: `153`

---

### P4 — JSON.parse + filter + optional chaining
```js
const rawEvents = [
  '{"type":"signup","user":{"name":"Alice","settings":{"notify":true}}}',
  '{"type":"signup","user":{"name":"Bob","settings":null}}',
  '{"type":"signup","user":{"name":"Carol"}}',
  '{"type":"purchase","user":{"name":"Dan","settings":{"notify":true}}}',
  '{"type":"signup","user":{"name":"Eve","settings":{"notify":false}}}',
];


const events = rawEvents.map(e => JSON.parse(e))
events.filter(e => e.type === "signup" && e.user?.settings?.notify === true )

```
1. Parse all events.
2. Filter only `"signup"` events where `user.settings.notify === true` (use `?.` for safety).

Expected: array containing only Alice's event object.

---

### P5 — Full pipeline: filter + map (destructuring) + reduce (group-by)
```js
const transactions = [
  { id: "TX-01", type: "credit", category: "salary", amount: 5000 },
  { id: "TX-02", type: "debit", category: "rent", amount: 1500 },
  { id: "TX-03", type: "debit", category: "food", amount: 200 },
  { id: "TX-04", type: "credit", category: "freelance", amount: 800 },
  { id: "TX-05", type: "debit", category: "food", amount: 150 },
  { id: "TX-06", type: "debit", category: "rent", amount: 1500 },
];

transactions.filter(t => t.type === "debit").map(({category, amount}) => ({category, amount})).reduce((acc,o) => {
  acc[o.category] = (acc[o.category] || 0) + o.amount
  return acc
},{})

//map(({category, amount}) => ({category, amount}))。这是正确的，告诉我原本的版本错误在哪里
```
1. Filter only `"debit"` transactions.
2. Map (with destructuring) to `{ category, amount }`.
3. Reduce to total amount per category.

Expected: `{ rent: 3000, food: 350 }`

---

## Part 3: File I/O Challenge (30 min)

### F1 — Read, transform, write

Create `exercises/week-01/practice-f1.js`.

Input file: `exercises/week-01/raw-leads.json` (same file from Exercise 03).

Task:
1. Read and parse the file.
2. Filter leads where `score >= 70` AND `email` is not empty (after trim).
3. Map to objects: `{ name, email (cleaned), grade }` where grade is:
   - score >= 90 → `"A"`
   - score >= 80 → `"B"`
   - score >= 70 → `"C"`
4. Write result to `exercises/week-01/practice-f1-output.json` (formatted).

Hint for grade: use ternary chaining — `score >= 90 ? "A" : score >= 80 ? "B" : "C"`

---

## Part 4: Memorization Pass (20 min)

Close all notes. Write each pattern from memory. Check yourself after.

### M1 — reduce sum
Write a reduce that sums an array of numbers: `[10, 20, 30, 40]` → `100`
numbers.reduce((acc,n) => acc + n, 0)

### M2 — reduce group-by
Write a reduce that groups by category (any made-up data).
data.reduce((acc,d) =>{
  acc[d.group] = acc[d.group] || []
  acc[d.group].push(d.name)
  return acc
},{})

### M3 — reduce find-max
Write a reduce that finds the object with the highest value (any made-up data).
data.reduce((acc,d) =>{
  acc = acc.score > d.score ? acc:d
  return acc
},{})


### M4 — map return object
Write a map that returns new objects with `()` syntax.
data.map(d => ({
  ...d,
  email:d.email.trim()
}))


### M5 — filter + some as guard
Write a function that uses `.some()` to check a condition first, then `.filter()` + `.reduce()` if safe.
function sumValidAmounts(data){
  if (!data.some(d => d.paid === true)){
    return 0 //这里return 0是为什么？是不是应该和return “unworthy to process”是一样的
  }
  return data
  .filter(d => d.paid === true)
  .reduce((acc,d) => acc+d.amount, 0)
}

### M6 — destructuring with alias + default
Write one line of destructuring that renames a field and provides a default.

const {name : userName, email= "abc@abc.com"} = leads


### M7 — spread copy + override
Write a spread that copies an object and overrides one field.

const newObj = {...oldObj, email: newemail}


### M8 — JSON full flow
Write the full flow: `require` → `readFileSync` → `JSON.parse` → transform → `JSON.stringify` → `writeFileSync`
const fs = require("fs")
const raw = fs.readFileSync("path", "utf-8")
const leads = JSON.parse(raw)
//transform
fs.writeFileSync("path", JSON.stringify(newLeads, null, 2))

---

## Part 5: Speed Round (20 min)

Answer as fast as possible. One-liners only.

### S1
`[3, 7, 1, 9, 4].filter(n => n > 5)` → ?
[7, 9]
### S2
`[{a:1},{a:2},{a:3}].map(x => x.a * 10)` → ?
[10, 20, 30]
### S3
`[1,2,3,4,5].reduce((s,n) => s + n, 0)` → ?
15
### S4
`[{x:1},{x:2},{x:3}].some(o => o.x > 5)` → ?
false
### S5
`[{x:1},{x:2},{x:3}].every(o => o.x > 0)` → ?
true
### S6
`const {a, b = 10} = {a: 5}` → a = ? b = ?
a = 5, b = 10
### S7
`{...{x:1, y:2}, y:99}` → ?
不知道
### S8
`"  HELLO  ".trim().toLowerCase()` → ?
"hello"
### S9
`const obj = {a: {b: null}}; obj.a.b?.c ?? "nope"` → ?
null
### S10
`[10,20,30].reduce((best, n) => n > best ? n : best)` → ?
30