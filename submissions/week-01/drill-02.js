const products = [
  { name: "  Widget A ", price: 29.99, category: "  TOOLS " },
  { name: "", price: 15.00, category: "parts" },
  { name: " Gadget B", price: 0, category: "ELECTRONICS " },
  { name: " Gizmo C ", price: 45.50, category: "  Tools" },
  { name: "Doohickey", price: 12.00, category: " electronics " },
];

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

console.log(cleanProducts(products));
