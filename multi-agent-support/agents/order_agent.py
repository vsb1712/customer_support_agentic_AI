def handle(query):
    if "order" in query.lower():
        return "Your order #1234 is out for delivery."
    return None
