# Filter & Map Drill 02 — New Scenario

## Scenario
You received raw product data from a supplier API. Some products have missing names or prices of 0. Clean the data before importing.

## Input
```js
const products = [
  { name: "  Widget A ", price: 29.99, category: "  TOOLS " },
  { name: "", price: 15.00, category: "parts" },
  { name: " Gadget B", price: 0, category: "ELECTRONICS " },
  { name: " Gizmo C ", price: 45.50, category: "  Tools" },
  { name: "Doohickey", price: 12.00, category: " electronics " },
];
```

## Requirements
Write a function `cleanProducts(products)` that:
1. **Reject** any product where name is empty (after trim) OR price is 0
2. **Clean** the valid products: trim name and category, lowercase category
3. Price stays as-is (it is a number, no need to transform)
4. Return `{ cleaned: [...], rejected: [...] }`

## Constraints
- Use .filter() and .map()
- Do not look at exercise-01

```js
function cleanProducts(products){
  const result = {
    cleaned:[],
    rejected:[]
  }
  
  result.cleaned = products.filter(product => product.name.trim() && product.price > 0)
  result.rejected = products.filter(product => !product.name.trim() || product.price === 0)
  result.cleaned = result.cleaned.map(product => {
    return {
      name:product.name.trim(),
      category:product.category.trim().toLowerCase(),
      price:product.price
    }
  })
  return result
}