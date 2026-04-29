const orders = [
  { id: "ORD-001", customer: "alice@test.com", product: "Widget", qty: 2, price: 25.00, status: "paid" },
  { id: "ORD-002", customer: "bob@test.com", product: "Gadget", qty: 1, price: 99.99, status: "pending" },
  { id: "ORD-003", customer: "alice@test.com", product: "Doohickey", qty: 5, price: 12.00, status: "paid" },
  { id: "ORD-004", customer: "carol@test.com", product: "Widget", qty: 1, price: 25.00, status: "cancelled" },
  { id: "ORD-005", customer: "dan@test.com", product: "Gadget", qty: 3, price: 99.99, status: "paid" },
  { id: "ORD-006", customer: "bob@test.com", product: "Widget", qty: 10, price: 25.00, status: "paid" },
  { id: "ORD-007", customer: "eve@test.com", product: "Doohickey", qty: 2, price: 12.00, status: "pending" },
];

// Write your function here
  function generateSummary(orders){
  const output = {
    totalRevenue:0,
    topCustomerEmail:"",
    ordersByStatus:{}
  }
  output.totalRevenue = orders.filter(o => o.status === "paid").reduce((total,o)=>{
    total = total + o.qty * o.price
    return total 
  },0)
  output.hasUnpaidOrders = orders.some(o => o.status !== "paid")
  output.allOrdersValid = orders.every(o => o.customer.trim() && o.price > 0)
  output.topCustomerEmail = orders.filter(o => o.status === "paid").reduce((acc,o) => {
    return acc.qty * acc.price > o.qty * o.price ? acc:o
  }).customer
  output.ordersByStatus = orders.reduce((acc,o) => {
    acc[o.status] = acc[o.status] || []
    acc[o.status].push(o.id)
    return acc
  },{})
  return output
}

// Test it
const result = generateSummary(orders);


// Expected output:
// {
//   totalRevenue: 659.97,
//   hasUnpaidOrders: true,
//   allOrdersValid: true,
//   topCustomerEmail: "dan@test.com",
//   ordersByStatus: {
//     paid: ["ORD-001", "ORD-003", "ORD-005", "ORD-006"],
//     pending: ["ORD-002", "ORD-007"],
//     cancelled: ["ORD-004"]
//   }
// }



const customer = {
  id: "C-001"
};

customer.id //"C-001"
customer.profile?.city//undefined
customer.profile.city//TypeError
customer.profile?.city ?? "unknown" //"unknown" 因为profile返回undefined，city返回error或者给出了的unknown