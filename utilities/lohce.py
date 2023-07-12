import requests
import hashlib

key = "rh8b2v4tLJ2avDBZ"
base_url = "https://lohce.com/apiusers/gettravels"
language = "fr";
version = "1.0";

def fetch_lohce(source, destination, schedules):
    # content = key + "douala" + "yaounde" + "12-07-2023" + language + version
    content = key + source + destination + schedules + language + version
    hash = hashlib.md5(content.encode()).hexdigest()
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
        base_url,
        data=data)