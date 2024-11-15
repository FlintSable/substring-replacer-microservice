# substring-replacer-microservice
A microservice for dynamically replacing words in a text with alternative words that contain the original as a substring. It accepts a block of text, processes each word, and returns a JSON response mapping each word to a substitute when available.

___
## Request Data
1. Prepare the request
- Crete a input.json file with a json object with "status": "pending" and a "words" list containing the words or phrases you want processed
- Example of json object in input.json file.
`
{
  "status": "pending",
  "words": [
    "tree",
    "rock",
    "water"
  ]
}
`
2. Submit the request:
- Write the JSON object to the input.json file to signal to the microservice that there is a new job to process.
3. Example call:
`
import json
request_data = {
"status": "pending",
"words": ["tree", "rock", "water"]
}

with open("input.json", "w") as file:
  json.dump(request_data, file, indent=2)
`


## Receive Data
1. Wait for completion:
- The substring substituter microservice will update input.json by changing the "status" keys value to "completed" when the job has been completed.
2. Read the processed data:
- Once the input.json file has "status": "completed", read the replacements field to view the results.
- Response Example
`
{
  "status": "completed",
  "words": [
    "tree",
    "rock",
    "water"
  ],
  "replacements": {
    "tree": "street",
    "rock": "rocket",
    "water": "watershed"
  }
}
`
3. Example call:
`
import json
while True:
  with open("input.json", "r") as file:
    res = json.load(file)

    if res.get("status") == "completed":
      print("Replacements:", res.get("replacements"))
      break
`
