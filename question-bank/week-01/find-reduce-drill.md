# Drill: .find() + .reduce()

## Basic (Q1–Q5)

### Q1 — find: Look up a contact
```js
const contacts = [
  { id: 101, email: "alice@test.com", name: "Alice" },
  { id: 102, email: "bob@test.com", name: "Bob" },
  { id: 103, email: "carol@test.com", name: "Carol" },
];
```
Use `.find()` to get the contact whose `email` is `"bob@test.com"`.
```js
const result = contacts.find(contact => contact.email === "bob@test.com")

---

### Q2 — reduce: Total price
```js
const lineItems = [
  { product: "Keyboard", price: 49.99 },
  { product: "Mouse", price: 29.99 },
  { product: "Monitor", price: 299.99 },
];
```
Use `.reduce()` to calculate the total price of all items.
```js
const result = lineItems.reduce((total,item) => {
  return total + item.price;
},0)

const result = lineItems.reduce((total,item) => total + item.price, 0)

```
---

### Q3 — reduce: Count by status
```js
const tasks = [
  { title: "Deploy API", status: "done" },
  { title: "Write tests", status: "todo" },
  { title: "Fix login bug", status: "done" },
  { title: "Update docs", status: "todo" },
  { title: "Code review", status: "in_progress" },
];
```
Use `.reduce()` to count how many tasks have `status === "done"`.
```js

const result = tasks.reduce((count,task) => {
  return task.status === "done" ? count +1:count;
} ,0)

```
---

### Q4 — find: First overdue invoice
```js
const invoices = [
  { id: "INV-001", amount: 500, overdue: false },
  { id: "INV-002", amount: 1200, overdue: true },
  { id: "INV-003", amount: 300, overdue: true },
];
```
Use `.find()` to get the first overdue invoice.
```js
const result = invoices.find(invoice => invoice.overdue === true);


```
---

### Q5 — reduce: Build a lookup object
```js
const employees = [
  { id: "E01", name: "Jun" },
  { id: "E02", name: "Mei" },
  { id: "E03", name: "Lei" },
];
```
Use `.reduce()` to create a lookup object: `{ "E01": "Jun", "E02": "Mei", "E03": "Lei" }`
```js

const lookup = employees.reduce((acc,employee) =>{
  acc[employee.id] = employee.name;
  return acc;
} ,{})

```
---

## Variants (Q6–Q10)

### Q6 — find + fallback
```js
const products = [
  { sku: "A100", name: "Widget", inStock: true },
  { sku: "A200", name: "Gadget", inStock: false },
  { sku: "A300", name: "Doohickey", inStock: true },
];
```
Use `.find()` to look up the product with `sku === "A999"`. If not found, return a default object: `{ sku: "A999", name: "Unknown", inStock: false }`.
```js
products.find(product => product.sku === "A999") || { sku: "A999", name: "Unknown", inStock: false } 



```
---

### Q7 — reduce: Group by source
```js
const leads = [
  { name: "Alice", source: "google", value: 500 },
  { name: "Bob", source: "referral", value: 300 },
  { name: "Carol", source: "google", value: 800 },
  { name: "Dan", source: "linkedin", value: 600 },
  { name: "Eve", source: "referral", value: 200 },
];
```
Use `.reduce()` to group lead names by source:
```js
{ google: ["Alice", "Carol"], referral: ["Bob", "Eve"], linkedin: ["Dan"] }
```
```js
leads.reduce((acc, lead) => {
  acc[lead.source] = acc[lead.source] || [];
  acc[lead.source].push(lead.name)
  return acc;
},{})

```
---

### Q8 — reduce: Find max
```js
const bids = [
  { bidder: "CompanyA", amount: 15000 },
  { bidder: "CompanyB", amount: 22000 },
  { bidder: "CompanyC", amount: 18000 },
];
```
Use `.reduce()` to find the bid with the highest amount. Return the whole object, not just the number.
```js

bids.reduce((highest,bid) => {
  return bid.amount > highest.amount ? bid : highest;
}, bids[0])

```
---

### Q9 — filter + reduce combo
```js
const orders = [
  { id: 1, status: "paid", total: 120 },
  { id: 2, status: "pending", total: 85 },
  { id: 3, status: "paid", total: 200 },
  { id: 4, status: "cancelled", total: 50 },
  { id: 5, status: "paid", total: 340 },
];
```
First `.filter()` only `"paid"` orders, then `.reduce()` to get the total revenue from paid orders.

```js
orders.filter(order => order.status === "paid").reduce((total,order) =>{
  total += order.total
  return total
} ,0)

```


---

### Q10 — reduce: Dedup by email
```js
const signups = [
  { email: "alice@test.com", name: "Alice", date: "2024-01-10" },
  { email: "bob@test.com", name: "Bob", date: "2024-01-11" },
  { email: "alice@test.com", name: "Alice W.", date: "2024-01-15" },
  { email: "carol@test.com", name: "Carol", date: "2024-01-12" },
  { email: "bob@test.com", name: "Robert", date: "2024-01-18" },
];
```
Use `.reduce()` to deduplicate by email — keep only the **first** signup for each email. Return an array of objects.
```js

signups.reduce((acc,signup) => {
  const exists = acc.find(item => item.email === signup.email);
  if (!exists){ 
  acc.push(signup);
  }
  return acc
}, [])

```