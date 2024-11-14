import json
import requests
import re

"""
n: TODO
    []: file reading
    []: file writting
    []: case sensitivity
"""

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
    """
    Finds replacement word using the datamuse api where the replacement contains the original word as a substring.
    Parameters:
        word (string): word to find replacement for
    Returns:
        str: replacement word containing the original word as a substring or original word if no replacement is found.
    """
    url = f"https://api.datamuse.com/words?sp=*{word}*"
    response = requests.get(url)

    if response.status_code != 200:
        print("error fetching from datamuse api")
        return word

    results = response.json()

    for item in results:
        replacement_word = item["word"]
        if word in replacement_word and replacement_word != word:
            return replacement_word
    return word

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
