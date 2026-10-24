
import re

from tools import (
    check_order_status,
    check_refund_status,
    search_faq,
)


def extract_order_id(message):
    match = re.search(r"\b\d{4,}\b", message)
    return match.group(0) if match else None


def customer_service_agent(message):
    message = message.strip()
    text = message.lower()

    if not message:
        return "Please enter your question."

    order_id = extract_order_id(message)

    # Refund questions
    if "refund" in text:
        if order_id:
            result = check_refund_status(order_id)

            if result["found"]:
                return (
                    f"Refund status for order {order_id}: "
                    f"{result['refund_status']}."
                )

            return f"Sorry, order {order_id} was not found."

        return "Please provide your order ID to check your refund."

    # Order tracking questions
    order_words = [
        "order", "delivery", "delivered",
        "shipping", "shipped", "track"
    ]

    if any(word in text for word in order_words):
        if order_id:
            result = check_order_status(order_id)

            if result["found"]:
                return (
                    f"Order {order_id} contains {result['product']}. "
                    f"Status: {result['status']}. "
                    f"Expected delivery: {result['expected_delivery']}."
                )

            return f"Sorry, order {order_id} was not found."

        return "Please provide your order ID to track your order."

    # FAQ questions
    faq_words = [
        "return", "cancel", "policy",
        "support", "contact", "business days"
    ]

    if any(word in text for word in faq_words):
        results = search_faq(message)

        if results != [
            "No matching FAQ found. Please contact support."
        ]:
            return "\n".join(results)

        return (
            "I couldn't find a matching answer. "
            "Please contact our support team."
        )

    return (
        "Hello! I'm your customer service assistant. "
        "I can help with order tracking, refunds, and FAQs. "
        "Try asking: 'Track order 1001' or "
        "'Check refund for order 1003'."
    )
  
