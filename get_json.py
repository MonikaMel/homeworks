import requests
import json

response = requests.get("https://swapi.dev/api/people/1/")
string_js = response.text
json_acceptable_string = string_js.replace("'", "\"")
data = json.loads(json_acceptable_string)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
