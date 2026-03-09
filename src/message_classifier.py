def classify_message(message):
    if message.startswith("[Server]"):
        return "server"
    elif message.startswith("[Client]"):
        return "client"
    else:
        return "unknown"
