import json

# Load tourism data
with open("tourism_data.json") as f:
    data = json.load(f)


# Function to format list nicely
def format_list(title, items):

    text = f"<b>{title}</b><br>"

    for item in items:
        text += f"• {item}<br>"

    text += "<br>"

    return text


# Main chatbot function
def get_response(query):

    query = query.lower()

    location = None

    # Detect location
    for place in data:
        if place in query:
            location = place
            break

    # If location not found
    if location is None:
        return "❌ Place not found. Try: Manali or Jaipur."

    place_data = data[location]

    response = f"<h3>📍 {location.title()}</h3>"

    # Detect category
    if "photo" in query or "photography" in query:

        response += format_list(
            "📸 Photography Spots",
            place_data["photography"]
        )

    elif "nature" in query:

        response += format_list(
            "🌿 Nature Spots",
            place_data["nature"]
        )

    elif "adventure" in query:

        response += format_list(
            "🏔 Adventure Activities",
            place_data["adventure"]
        )

    elif "religious" in query or "temple" in query:

        response += format_list(
            "🛕 Religious Places",
            place_data["religious"]
        )

    elif "stay" in query or "hotel" in query:

        stay = place_data["stay"]

        response += "<b>🏨 Stay Options</b><br><br>"

        response += "<b>Budget</b><br>"
        for hotel in stay["budget"]:
            response += f"• {hotel}<br>"

        response += "<br><b>Mid Range</b><br>"
        for hotel in stay["mid"]:
            response += f"• {hotel}<br>"

        response += "<br><b>Luxury</b><br>"
        for hotel in stay["luxury"]:
            response += f"• {hotel}<br>"

    else:

        # If user only gives place name show everything

        response += format_list(
            "📸 Photography Spots",
            place_data["photography"]
        )

        response += format_list(
            "🌿 Nature Spots",
            place_data["nature"]
        )

        response += format_list(
            "🏔 Adventure Activities",
            place_data["adventure"]
        )

        response += format_list(
            "🛕 Religious Places",
            place_data["religious"]
        )

    return response