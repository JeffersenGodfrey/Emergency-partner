# nlp_engine.py

def detect_emergency(text):
    """
    Detect the type of emergency based on keywords in the user's input.

    Parameters:
    - text (str): User's input description

    Returns:
    - str: One of the categories: "Medical Emergency", "Flood Help", or "Charging Station"
    """
    text = text.lower()

    # Medical emergencies
    medical_keywords = [
        "ambulance", "oxygen", "emergency", "injury", "doctor",
        "hospital", "medic", "covid", "icu", "blood", "sick"
    ]

    # Flood or disaster relief
    flood_keywords = [
        "flood", "water", "shelter", "rain", "relief", "rescue",
        "food", "help", "disaster", "emergency food"
    ]

    # Charging and power
    charging_keywords = [
        "charge", "charging", "electricity", "battery", "power",
        "phone dead", "generator", "mobile charge", "fuel", "petrol"
    ]

    # Keyword detection
    for word in medical_keywords:
        if word in text:
            return "Medical Emergency"

    for word in flood_keywords:
        if word in text:
            return "Flood Help"

    for word in charging_keywords:
        if word in text:
            return "Charging Station"

    # Default fallback
    return "Medical Emergency"
