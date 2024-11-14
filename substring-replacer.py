import json
import requests
import re



def process_text(text):
    """
    Processes the input and formats it for the find_replacement function.
    Parameters:
        text (string or list)
    Returns:
        dict: a dictionary where the keys are the original word and values is the replacement word.
    """
    if isinstance(text, str):
        words = re.findall(r'\b\w+\b', text)
    elif isinstance(text, list):
        words = text
    else:
        raise ValueError("Input must be a string or a list of words")

    replacements = {word: find_replacement(word) for word in words}
    return replacements


def find_replacement(word):
    # datamuse api part
    print("needs to be implemented")
    pass

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
