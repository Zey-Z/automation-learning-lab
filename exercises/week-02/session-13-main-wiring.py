"""
Session 13 - Main Wiring Drill

Goal: practice orchestrating a script with main().
Do not rewrite the helper functions first. Start with main().

Input file:
exercises/week-02/session-13-orders.json

Output file:
exercises/week-02/session-13-order-summary.json
"""

import json

INPUT_PATH = "exercises/week-02/session-13-orders.json"
OUTPUT_PATH = "exercises/week-02/session-13-order-summary.json"


def load_orders(path):
    with open(path, "r") as f:
        return json.load(f)


def filter_paid_orders(orders):
    return [order for order in orders if order["status"] == "paid"]


def build_summary(orders):
    return {
        "paidCount": len(orders),
        "totalAmount": sum(order["amount"] for order in orders),
        "highValueCustomers": [
            order["customer"] for order in orders if order["amount"] >= 100
        ],
    }


def save_summary(summary, path):
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)


def main():
    """
    Write the orchestration only:
    1. load orders from INPUT_PATH
    2. keep only paid orders
    3. build a summary
    4. save the summary to OUTPUT_PATH
    5. print the summary
    """

    # Your code here
    orders = load_orders(INPUT_PATH)
    paid_orders = filter_paid_orders(orders)
    summary = build_summary(paid_orders)
    save_summary(summary, OUTPUT_PATH)

    print(summary) 


if __name__ == "__main__":
    main()
