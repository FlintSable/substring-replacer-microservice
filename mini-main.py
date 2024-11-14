import json
import time

# n: mini sample program
# programatically sending inputs to the substring_replacer microservice
# uses inputs.json as communication pipeline

text_inputs = [
    {
    "status": "pending",
    "words": ["tree","rock","water"
    ]
    },
    {
    "status": "pending",
    "words": ["cat","dog","bird","apple"
    ]
    },
    {
    "status": "pending",
    "words": [
        "The cat sat on the mat."
    ]
    },
    {
    "status": "pending",
    "words": ["The cat sat on the mat.","rock","apple pie"
    ]
    }
]

def write_input(input):
    with open("input.json", "w") as file:
        json.dump(input, file, indent=2)

def read_output():
    with open("input.json", "r") as file:
        return json.load(file)

def main():
    for input in text_inputs:
        print(f"processing: {input['words']}")
        write_input(input)

        while True:
            output = read_output()
            if output.get("status") == "completed":
                print("replacements:", output.get("replacements"))
                print()
                break
            time.sleep(3)

if __name__ == "__main__":
    main()
