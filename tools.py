
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_orders():
    with open(DATA_DIR / "orders.json", "r", encoding="utf-8") as file:
        return json.load(file)


def check_order_status(order_id):
    orders = load_orders()

    for order in orders:
        if order["order_id"] == str(order_id):
            return {
                "found": True,
                "order_id": order["order_id"],
                "product": order["product"],
                "status": order["status"],
                "expected_delivery": order["expected_delivery"]
            }

    return {"found": False, "message": "Order not found."}


def check_refund_status(order_id):
    orders = load_orders()

    for order in orders:
        if order["order_id"] == str(order_id):
            return {
                "found": True,
                "order_id": order["order_id"],
                "refund_status": order["refund_status"]
            }

    return {"found": False, "message": "Order not found."}


def search_faq(keyword):
    with open(DATA_DIR / "faq.json", "r", encoding="utf-8") as file:
        faqs = json.load(file)

    keyword = keyword.lower()

    results = [
        faq["answer"]
        for faq in faqs
        if keyword in faq["question"].lower()
        or keyword in faq["answer"].lower()
    ]

    if results:
        return results

    return ["No matching FAQ found. Please contact support."]
  
