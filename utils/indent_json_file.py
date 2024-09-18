import json

file_to_rewrite = "dota_match.json"

with open(file_to_rewrite, "r") as file:
    json_to_change = json.load(file)
with open(file_to_rewrite, "w") as file:
    json.dump(json_to_change, file, indent=4)
