import json

def get_resources(category):
    with open("data/emergency_data.json", "r") as file:
        data = json.load(file)
    
    return [d for d in data if d["category"] == category and d["is_open"]]