import json
import os

FAQ_FILE = "data/faq.json"

def handle(query):
    # If file missing or empty → don't crash system
    if not os.path.exists(FAQ_FILE) or os.path.getsize(FAQ_FILE) == 0:
        return None

    try:
        with open(FAQ_FILE, "r") as f:
            faq = json.load(f)
    except json.JSONDecodeError:
        return None  # Prevents server crash

    query = query.lower()

    for key in faq:
        if key in query:
            return faq[key]

    return None
