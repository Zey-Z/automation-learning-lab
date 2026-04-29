orders = [
    {"id": "O1", "customer": "Alice", "amount": 120, "status": "paid"},
    {"id": "O2", "customer": "Bob",   "amount": 50,  "status": "pending"},
    {"id": "O3", "customer": "Carol", "amount": 300, "status": "paid"},
    {"id": "O4", "customer": "Dan",   "amount": 75,  "status": "paid"},
]


for order in orders:
    if order["status"] == "paid":
        print(f"{order['customer']} {order['status']} ${order['amount']}")