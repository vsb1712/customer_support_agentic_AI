import json, os, uuid

TICKET_FILE = "data/tickets.json"

def handle(query):
    ticket_id = str(uuid.uuid4())[:6]

    if not os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, "w") as f:
            json.dump({}, f)

    try:
        with open(TICKET_FILE, "r") as f:
            data = json.load(f)
    except:
        data = {}

    data[ticket_id] = query

    with open(TICKET_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return f"I've created a support ticket. ID: {ticket_id}"
