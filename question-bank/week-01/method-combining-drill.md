# Drill: Method Combining — All 6 Array Methods

Practice mixing `.filter()`, `.map()`, `.find()`, `.reduce()`, `.some()`, `.every()` in realistic automation scenarios.

Reminder:
- **Data tools** (filter, map, reduce) → return arrays/values, can chain
- **Decision tools** (some, every) → return boolean, use with `if`
- **Lookup tool** (find) → return single item or `undefined`

---

## Basic (Q1–Q5)

### Q1 — reduce: Total hours logged
```js
const timeLogs = [
  { employee: "Alice", project: "CRM", hours: 4.5 },
  { employee: "Bob", project: "CRM", hours: 3.0 },
  { employee: "Alice", project: "API", hours: 2.0 },
  { employee: "Carol", project: "CRM", hours: 5.5 },
  { employee: "Bob", project: "API", hours: 1.5 },
];
```
Use `.reduce()` to calculate the total hours logged across all entries.
```js
timeLogs.reduce((total,timelog) => total += timelog.hours, 0)
```
---

### Q2 — filter + map: Clean email list
```js
const subscribers = [
  { email: "  Alice@Test.COM ", active: true },
  { email: "bob@test.com", active: false },
  { email: " CAROL@test.com  ", active: true },
  { email: "", active: true },
  { email: "dan@test.com", active: true },
];
```
Filter only `active` subscribers who have a non-empty `email`, then map to an array of lowercase trimmed emails.

Expected: `["alice@test.com", "carol@test.com", "dan@test.com"]`
```js
result = subscribers.filter(subscriber => subscriber.active && subscriber.email.trim()).map(subscriber => subscriber.email.trim().toLowerCase())
```


---

### Q3 — find + fallback: Lookup config
```js
const configs = [
  { key: "retry_limit", value: 3 },
  { key: "timeout_ms", value: 5000 },
  { key: "batch_size", value: 100 },
];
```
Write a function `getConfig(configs, key)` that uses `.find()` to look up a config by key. If not found, return `{ key: key, value: null }`.

Test with: `getConfig(configs, "timeout_ms")` and `getConfig(configs, "log_level")`
```js
function getConfig(configs, key){
  return configs.find(config => config.key === key) || { key: key, value: null };
}
```
---

### Q4 — reduce: Count by category
```js
const tickets = [
  { id: 1, category: "billing", resolved: true },
  { id: 2, category: "technical", resolved: false },
  { id: 3, category: "billing", resolved: false },
  { id: 4, category: "general", resolved: true },
  { id: 5, category: "technical", resolved: true },
  { id: 6, category: "billing", resolved: true },
];
```
Use `.reduce()` to count the number of tickets per category.

Expected: `{ billing: 3, technical: 2, general: 1 }`
```js
function countforTicket(tickets){
  const result = tickets.reduce((acc,ticket)=> {
  acc[ticket.category] = (acc[ticket.category] || 0) + 1 
  return acc
  },{});
  return result
}

```


---

### Q5 — some + every: Validation check
```js
const shipments = [
  { id: "SH-01", weight: 12, destination: "NYC", insured: true },
  { id: "SH-02", weight: 45, destination: "LA", insured: true },
  { id: "SH-03", weight: 5, destination: "", insured: false },
  { id: "SH-04", weight: 30, destination: "CHI", insured: true },
];
```
Answer two questions using array methods:
1. Are there any shipments with an empty `destination`? (use `.some()`)
2. Are all shipments with `weight > 10` insured? (use `.filter()` + `.every()`)
```js

shipments.some(shipment => !shipment.destination.trim())
shipments.filter(shipment => shipment.weight > 10).every(shipment => shipment.insured)

```
---

## Variants (Q6–Q10)

### Q6 — filter + reduce: Revenue by region
```js
const sales = [
  { rep: "Alice", region: "West", amount: 5000, status: "closed" },
  { rep: "Bob", region: "East", amount: 3000, status: "closed" },
  { rep: "Carol", region: "West", amount: 7000, status: "pending" },
  { rep: "Dan", region: "East", amount: 4500, status: "closed" },
  { rep: "Eve", region: "West", amount: 2000, status: "closed" },
];
```
First `.filter()` only `"closed"` deals, then `.reduce()` to get total revenue grouped by region.

Expected: `{ West: 7000, East: 7500 }`
```js
sales.filter(sale => sale.status === "closed").reduce((acc,sale) => {
  acc[sale.region] = (acc[sale.region] || 0) + sale.amount
  return acc
}, {})


```
---

### Q7 — some (as guard) + filter + reduce: Safe batch processing
```js
const payments = [
  { id: "P-01", amount: 500, currency: "USD", verified: true },
  { id: "P-02", amount: 150, currency: "USD", verified: true },
  { id: "P-03", amount: -50, currency: "USD", verified: true },
  { id: "P-04", amount: 300, currency: "USD", verified: false },
  { id: "P-05", amount: 200, currency: "USD", verified: true },
];
```
Step 1: Use `.some()` to check if any payment has a negative `amount`. If yes, return `{ error: "Negative payment detected", total: 0 }`.
Step 2: If no negatives, `.filter()` only `verified` payments, then `.reduce()` to calculate the total.

This is the **decision tool + data tool** pattern: `.some()` makes the decision, then `if/else` controls whether data tools run.
```js
function Q7(payments){
  if (payments.some(payment => payment.amount <0)){
  return { error: "Negative payment detected", total: 0 }
  }else{ return payments.filter(payment => payment.verified === true).reduce((acc,p)=> {
    acc = acc + p.amount
    return acc
  },0)
}
}
```
---

### Q8 — filter + map + reduce: Pipeline
```js
const apiLogs = [
  { endpoint: "/users", status: 200, responseTime: 120, method: "GET" },
  { endpoint: "/orders", status: 500, responseTime: 3500, method: "POST" },
  { endpoint: "/users", status: 200, responseTime: 95, method: "GET" },
  { endpoint: "/orders", status: 200, responseTime: 200, method: "POST" },
  { endpoint: "/health", status: 200, responseTime: 15, method: "GET" },
  { endpoint: "/orders", status: 500, responseTime: 4200, method: "POST" },
];
```
Build a 3-step pipeline:
1. `.filter()` — only failed requests (`status !== 200`)
2. `.map()` — extract `{ endpoint, responseTime }`
3. `.reduce()` — calculate average response time of failed requests

```js
const result = apiLogs.filter(apiLog => apiLog.status !== 200).map(a => ({
  endpoint : a.endpoint,
  responseTime : a.responseTime 
  }))
const total = result.reduce((acc,t) => {
  acc = acc + t.responseTime
  return acc
},0 )

const ave = total / result.length

```


---

### Q9 — every (as guard) + find + map: Conditional processing
```js
const candidates = [
  { name: "Alice", score: 85, interviewed: true },
  { name: "Bob", score: 92, interviewed: true },
  { name: "Carol", score: 78, interviewed: true },
  { name: "Dan", score: 95, interviewed: true },
];
```
Step 1: Use `.every()` to check if all candidates have been `interviewed`.
Step 2: If yes, use `.find()` to get the candidate with the highest `score` (hint: you can sort first, or use reduce).
Step 3: Use `.map()` to create a summary array: `["Alice: 85", "Bob: 92", ...]` using template literals.

Return an object: `{ allInterviewed: true/false, topCandidate: "...", summary: [...] }`
```js
function Q9(candidates){
  const result = {
    topCandidate: "" ,
    summary:[]
  }
  if (candidates.every(c => c.interviewed === true)){
    result.allInterviewd = true
    
  const top = candidates.reduce((best,c) => c.score > best.score ? c: best)
  result.topCandidate = top.name

  result.summary = candidates.map(c => `${c.name}: ${c.score}`)
  }
  return result 
}


```
---

### Q10 — Full pipeline: Webhook event processor
```js
const webhookEvents = [
  { type: "order.created", payload: { orderId: "A1", amount: 150 }, timestamp: "2024-03-01T10:00:00Z", processed: false },
  { type: "order.created", payload: { orderId: "A2", amount: 300 }, timestamp: "2024-03-01T10:05:00Z", processed: false },
  { type: "order.cancelled", payload: { orderId: "A3", amount: 75 }, timestamp: "2024-03-01T10:10:00Z", processed: true },
  { type: "order.created", payload: { orderId: "A4", amount: 500 }, timestamp: "2024-03-01T10:15:00Z", processed: false },
  { type: "payment.received", payload: { orderId: "A1", amount: 150 }, timestamp: "2024-03-01T10:20:00Z", processed: false },
  { type: "order.created", payload: { orderId: "A5", amount: 200 }, timestamp: "2024-03-01T10:25:00Z", processed: true },
];
```
Write a function `processWebhooks(events)` that returns:

1. `unprocessedOrders` — `.filter()` events where `type === "order.created"` AND `processed === false`, then `.map()` to extract just `{ orderId, amount }` from the payload.

2. `totalUnprocessedValue` — `.reduce()` the unprocessed orders to get total amount.

3. `hasPayments` — `.some()` to check if any event has `type === "payment.received"`.

4. `allProcessed` — `.every()` to check if all events have `processed === true`.

Expected:
```js
{
  unprocessedOrders: [
    { orderId: "A1", amount: 150 },
    { orderId: "A2", amount: 300 },
    { orderId: "A4", amount: 500 }
  ],
  totalUnprocessedValue: 950,
  hasPayments: true,
  allProcessed: false
}

function Q10(webhookEvents){
  const result = {
    unprocessedOrders:[],
    totalUnprocessedValue: 0,
    hasPayments: webhookEvents.some(e => e.type === "payment.received"),
    allProcessed: webhookEvents.every(e => e.processed === true)
  }

  result.unprocessedOrders = webhookEvents.filter(
    e => e.type ==="order.created" && e.processed === false)
    .map(e => e.payload)
  const total = result.unprocessedOrders.reduce ((acc,a) => {
    acc = acc + a.amount
    return acc
  },0)
  
  result.totalUnprocessedValue = total
  return result
}

```

```js
const tickets = [
  { id: "T-01", title: "Login broken", priority: "high" },
  { id: "T-02", title: "Typo on homepage", priority: "low" },
  { id: "T-03", title: "Payment fails", priority: "high" },
  { id: "T-04", title: "Slow dashboard", priority: "medium" },
  { id: "T-05", title: "Wrong email sent", priority: "medium" },
];

tickets.reduce((acc,ticket) =>{
  acc[ticket.priority] = acc[ticket.priority] || []
  acc[ticket.priority].push(ticket.id)
  return acc
},{})

const reps = [
  { name: "Alice", deals: 12 },
  { name: "Bob", deals: 27 },
  { name: "Carol", deals: 19 },
  { name: "Dan", deals: 8 },
];

reps.reduce((acc,rep) => rep.deals > acc.deals ? rep:acc).name 

const employees = [
  { firstName: "Alice", lastName: "Chen", department: "Engineering" },
  { firstName: "Bob", lastName: "Kim", department: "Sales" },
  { firstName: "Carol", lastName: "Park", department: "Engineering" },
];

employees.map( e=> ({
  fullName: `${e.firstName} ${e.lastName}`,
  label: `${e.firstName} ${e.lastName} (${e.department})`
}))

```