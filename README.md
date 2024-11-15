# substring-replacer-microservice
A microservice for dynamically replacing words in a text with alternative words that contain the original as a substring. It accepts a block of text, processes each word, and returns a JSON response mapping each word to a substitute when available.

___
## Request Data
1. Crete a input.json file with a json object with "status": "pending" and a "words" list containing the words or phrases you want processed
Example of json object in input.json file.
`code`
{
  "status": "pending",
  "words": [
    "tree",
    "rock",
    "water"
  ]
}
`code`


## Receive Data
