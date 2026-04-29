# Drill: Objects + JSON — Access, Destructure, Transform

Practice object access, destructuring, spread, JSON parsing, optional chaining, and nullish coalescing in realistic automation scenarios.

---

## Basic (Q1–Q5)

### Q1 — Dot vs bracket notation
```js
const lead = { name: "Alice Chen", source: "webinar", score: 82 };
const field = "score";
```
Write two expressions:
1. Get the lead's `name` using dot notation.
2. Get the lead's score using bracket notation with the `field` variable.
```js
lead.name
lead[field]
```
---

### Q2 — Destructuring with alias and default
```js
const apiResponse = {
  user_id: "U-4521",
  email: "bob@acme.com",
  role: "viewer"
};

const { user_id:userId, email, plan = "free"} = apiResponse //我理解destructuring是一种用{}来选取obj内的变量的方式，等号右边是{}里面的这些内容是属于这个obj的意思
```
In one line of destructuring:
- Extract `user_id` and rename it to `userId`
- Extract `email`
- Extract `plan` with a default value of `"free"`

---

### Q3 — Spread operator: update without mutating
```js
const ticket = {
  id: "TK-100",
  status: "open",
  assignee: "Carol",
  priority: "low"
};

const updatedTicket = {
  ...ticket,
  status: "in_progress",
  priority: "high"
}
```
Create a new object `updatedTicket` that copies everything from `ticket` but changes `status` to `"in_progress"` and `priority` to `"high"`. Do NOT modify the original `ticket`.

---

### Q4 — JSON.parse + nested access
```js
const raw = '{"order":{"id":"ORD-77","customer":{"name":"Dan","email":"dan@test.com"},"items":[{"product":"Widget","qty":3}]}}';

const parsed = JSON.parse(raw)
const email = parsed.order.customer.email
const itemsName = parsed.order.items[0].product

```
1. Parse `raw` into an object.
2. Get the customer's email.
3. Get the first item's product name.

---

### Q5 — Optional chaining + nullish coalescing
```js
const contacts = [
  { name: "Eve", address: { city: "Seattle", zip: "98101" } },
  { name: "Frank", address: null },
  { name: "Grace" },
];
city1 = contacts[0].address.city
city2 = contacts[1].address ?? "Unknown" //我是因为看到原始数据里面没有city，我就不用.address?.city ?? 了，但是其实这个写成city3的样子也正确
city3 = contacts[2].address?.city ?? "Unknown"

```
For each contact, write an expression that gets their city. If the city is missing for any reason (no address, address is null, no city property), return `"Unknown"`.

Hint: use `?.` and `??` together.

---

## Variants (Q6–Q10)

### Q6 — Destructuring in filter + map callback
```js
const employees = [
  { name: "Alice", department: "Engineering", salary: 95000 },
  { name: "Bob", department: "Sales", salary: 72000 },
  { name: "Carol", department: "Engineering", salary: 110000 },
  { name: "Dan", department: "Sales", salary: 68000 },
  { name: "Eve", department: "Engineering", salary: 88000 },
];

const highEarner = employees.filter(({department,salary}) => department === "Engineering" && salary > 90000)
.map(({name,salary}) => `${name}:$${salary}`)//这里有点卡住不知道=>右边该是什么，本来写的是name：salary，看了你的提示之后才改对


```
Using destructuring in the callback parameters:
1. `.filter()` only Engineering employees with salary > 90000.
2. `.map()` to an array of strings: `"Alice: $95,000"` (use template literal; don't worry about exact number formatting, just `salary`).

Expected: `["Alice: $95000", "Carol: $110000"]`

---

### Q7 — Bracket notation with dynamic key + reduce
```js
const events = [
  { type: "click", page: "/home" },
  { type: "scroll", page: "/home" },
  { type: "click", page: "/pricing" },
  { type: "click", page: "/home" },
  { type: "scroll", page: "/pricing" },
];

const groupBy = "type"; // this could also be "page"
result = events.reduce((acc,e) => {
  acc[e[groupBy]] = (acc[e[groupBy]] || 0)  + 1
  return acc
},{})


```
Use bracket notation with the `groupBy` variable to `.reduce()` events into a count object.

When `groupBy = "type"`: `{ click: 3, scroll: 2 }`
When `groupBy = "page"`: `{ "/home": 3, "/pricing": 2 }`

---

### Q8 — Spread + map: enrich data
```js
const users = [
  { id: 1, name: "Alice", email: "alice@test.com" },
  { id: 2, name: "Bob", email: "bob@test.com" },
  { id: 3, name: "Carol", email: "carol@test.com" },
];
```
Use `.map()` with spread to create a new array where each user object gets two new fields: `role: "member"` and `active: true`. Do not modify the original array.

Expected first item: `{ id: 1, name: "Alice", email: "alice@test.com", role: "member", active: true }`
```js
users.map(u => ({
  ...u,
  role:"member",
  active: true
}))


```
---

### Q9 — JSON.parse + optional chaining + filter
```js
const rawPayloads = [
  '{"event":"signup","user":{"name":"Alice","preferences":{"newsletter":true}}}',
  '{"event":"signup","user":{"name":"Bob"}}',
  '{"event":"signup","user":{"name":"Carol","preferences":{"newsletter":false}}}',
  '{"event":"signup","user":{"name":"Dan","preferences":null}}',
];
rawPayloads.map(l=> JSON.parse(l)
).filter(l => l.user?.preferences?.newsletter === true)


```
1. `.map()` each raw string into a parsed object.
2. `.filter()` only users who opted into the newsletter. Safely handle cases where `preferences` is missing or null.

Expected result: array containing only Alice's parsed object.

---

### Q10 — Full pipeline: normalize API response
```js
const apiData = '{"results":[{"employee_id":"E-001","full_name":"Alice Chen","dept":"ENG","compensation":{"base":95000,"bonus":8000}},{"employee_id":"E-002","full_name":"Bob Kim","dept":"SALES","compensation":{"base":72000}},{"employee_id":"E-003","full_name":"Carol Park","dept":"ENG","compensation":{"base":110000,"bonus":15000}}]}';
```
Write a function `normalizeEmployees(apiData)` that:
1. Parses the JSON string.
2. Uses `.map()` with destructuring to transform each employee into:
```js
{
  id: "E-001",           // renamed from employee_id
  name: "Alice Chen",    // renamed from full_name
  department: "ENG",     // renamed from dept
  totalPay: 103000       // base + bonus (bonus defaults to 0 if missing)
}
```
3. Uses `.filter()` to keep only employees with `totalPay > 100000`.
4. Returns the filtered array.

Expected:
```js
[
  { id: "E-001", name: "Alice Chen", department: "ENG", totalPay: 103000 },
  { id: "E-003", name: "Carol Park", department: "ENG", totalPay: 125000 }
]
```
```js
function normalizeEmployees(apiData){
  const parsed = JSON.parse(apiData)
  const {compensation = {base,bonus = 0}} = employee
  const result = parsed.results.map(({employee_id,full_name,dept,compensation:`${base} + ${bonus}`}) => ({ //这里compensation的表达不知道对不对，以及这里=>的括号我觉得应该加上不应该只有一个{}
    id:employee_id,
    name:full_name,
    department:dept,
    totalPay:compensation
  })).filter(e=> e.totalPay > 100000)
  return result
}
```