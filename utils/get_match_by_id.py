import requests
import json


OPENDOTA_API_URL = "https://api.opendota.com/api"

match_id = 7947857043

d_match = requests.get(f"{OPENDOTA_API_URL}/matches/{match_id}")
with open(f"dota_match_{match_id}.json", "w") as f_to_write:
    f_to_write.write(json.dumps(d_match.json()))