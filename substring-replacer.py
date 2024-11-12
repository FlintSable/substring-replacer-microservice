import json
import requests
import re

def process_request():
    filename = "input.json"
    with open(filename, "r") as file:
        data = json.load(file)

    if data.get("status") == "pending":
        replacements = process_text("".join(data["words"]))

        data["status"] = "completed"
        data["replacements"] = replacements

        with open(filename, "w") as file:
            json.dump(data, file, indent=2)


if __name__=="__main__":
    process_request()
