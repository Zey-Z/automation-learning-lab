# Filter & Map Drill Set 01

Do each one independently. No looking at the previous answer.

## Q1 — filter only
Given:
```js
const users = [
  { name: "Alice", active: true },
  { name: "Bob", active: false },
  { name: "Charlie", active: true },
  { name: "Dave", active: false },
];

users.filter(user => user.active)
```
Write one line: get an array of only the active users.

## Q2 — map only
Given:
```js
const prices = [10, 20, 35, 50];

prices.map(price => price *1.08)

```
Write one line: get a new array where every price has 8% tax added (multiply by 1.08).

## Q3 — filter + map
Given:
```js
const orders = [
  { id: 1, total: 250, status: "paid" },
  { id: 2, total: 80, status: "pending" },
  { id: 3, total: 500, status: "paid" },
  { id: 4, total: 120, status: "paid" },
  { id: 5, total: 30, status: "pending" },
];

function processOrders(orders){
  const result = {
    paid: []
  }
  result.paid = orders.filter(order => order.status === "paid")
  result.paid = result.paid.map(order => {
    return {
      id: order.id,
      total: order.total
    }
  })
  return result;
}

```
Get an array of only the paid orders, but return just the id and total (not status).

## Q4 — filter with string method
Given:
```js
const emails = [
  "  alice@test.com ",
  "",
  "BOB@EXAMPLE.COM",
  "   ",
  "charlie@test.com",
];

let A =[]
A = emails.filter(email => email.trim())
A = A.map(email => email.trim().toLowerCase())

```
Get an array of only the non-empty emails (after trimming), all lowercased and trimmed.

## Q5 — map returning new object
Given:
```js
const raw = [
  { first: "Alice", last: "Wang", dept: "sales" },
  { first: "Bob", last: "Li", dept: "engineering" },
  { first: "Charlie", last: "Chen", dept: "sales" },
];

let B = []
B = raw.map(worker => {
  return{
  fullName: worker.first + " " + worker.last,
  dept : worker.dept
  }
}) 

```
Use .map() to return an array of objects with this shape:
```js
{ fullName: "Alice Wang", dept: "sales" }
```
Hint: you can combine strings with `+` or template literals.
