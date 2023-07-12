import requests
import hashlib

key = "rh8b2v4tLJ2avDBZ"
base_url = "https://lohce.com/apiusers/gettravels"
headers = {"Content-Type": "application/json"}
language = "fr";
version = "1.0";

def fetch_lohce(source, destination, schedules):
    content = key + source + destination + schedules + language + version
    hash = hashlib.md5(content.encode());
    data = {
        "api_key"     : key,
        "departure"   : source,
        "arrival"     : destination, 
        "date"        : schedules,
        "language"    : language,
        "version"     : version,
        "hash"        : hash,
    }

    return requests.post(
        base_url + "/upload",
        headers=headers,
        data=data)