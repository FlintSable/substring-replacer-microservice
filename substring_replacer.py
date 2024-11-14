import json
import time
import requests
import re

"""
n: TODO
    [x]: file reading
    [x]: file writting
    []: case sensitivity
"""

def process_text(word_list):
    """
    Processes the input and formats it for the find_replacement function.
    Parameters:
        text (list)
    Returns:
        dict: a dictionary where the keys are the original word and values is the replacement word.
    """
    replacements = {}
    for item in word_list:
        # n: regex: \b word boundry, \w matches any word char, + one or more
        words = re.findall(r'\b\w+\b', item) if " " in item else [item]

        for word in words:
            replacements[word] = find_replacement(word)
    return replacements


def find_replacement(word):
    """
    Finds replacement word using the datamuse api where the replacement contains the original word as a substring.
    Parameters:
        word (string): word to find replacement for
    Returns:
        str: replacement word containing the original word as a substring or original word if no replacement is found.
    """
    # n: sp is spelled like, * is wild
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
        replacements = process_text(data["words"])
        # print(replacements)
        # n: update json data
        data["status"] = "completed"
        data["replacements"] = replacements

        # n: write updates to file
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)


if __name__=="__main__":
    while True:
        process_request()
        print("\nchecking")
        for i in range(2):
            print("waiting...", i)
            time.sleep(1)
