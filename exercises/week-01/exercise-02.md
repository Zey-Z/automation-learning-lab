# Exercise 02 — Order Summary Generator

## Scenario
You work on an automation team. Every day, an order system dumps raw order data.
Your job: write a function that takes raw orders and produces a business summary.

## Input
```js
const orders = [
  { id: "ORD-001", customer: "alice@test.com", product: "Widget", qty: 2, price: 25.00, status: "paid" },
  { id: "ORD-002", customer: "bob@test.com", product: "Gadget", qty: 1, price: 99.99, status: "pending" },
  { id: "ORD-003", customer: "alice@test.com", product: "Doohickey", qty: 5, price: 12.00, status: "paid" },
  { id: "ORD-004", customer: "carol@test.com", product: "Widget", qty: 1, price: 25.00, status: "cancelled" },
  { id: "ORD-005", customer: "dan@test.com", product: "Gadget", qty: 3, price: 99.99, status: "paid" },
  { id: "ORD-006", customer: "bob@test.com", product: "Widget", qty: 10, price: 25.00, status: "paid" },
  { id: "ORD-007", customer: "eve@test.com", product: "Doohickey", qty: 2, price: 12.00, status: "pending" },
];
```

## Task
Write a function `generateSummary(orders)` that returns an object with:

### 1. `totalRevenue`
Total revenue from **paid** orders only. Revenue per order = `qty * price`.

### 2. `hasUnpaidOrders`
Boolean — are there any orders that are NOT "paid"?

### 3. `allOrdersValid`
Boolean — does every order have a non-empty `customer` and `price > 0`?

### 4. `topCustomerEmail`
The email of the customer who spent the most (paid orders only). Use reduce to find the max spender.

### 5. `ordersByStatus`
Group orders by status. Each key = status, value = array of order IDs.
Example: `{ paid: ["ORD-001", "ORD-003", ...], pending: [...], ... }`

## Expected Output
```js
{
  totalRevenue: 610.97,
  hasUnpaidOrders: true,
  allOrdersValid: true,
  topCustomerEmail: "dan@test.com",
  ordersByStatus: {
    paid: ["ORD-001", "ORD-003", "ORD-005", "ORD-006"],
    pending: ["ORD-002", "ORD-007"],
    cancelled: ["ORD-004"]
  }
}
```

## Requirements
- Use `.filter()`, `.map()`, `.reduce()`, `.find()`, `.some()`, `.every()` — all 6.
- Write it as one function.
- Do not use for loops.

## Rubric
- Correctness: output matches expected (5 pts)
- Uses all 6 array methods appropriately (3 pts)
- Code is readable and well-structured (2 pts)
