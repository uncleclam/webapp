from datetime import datetime
import json
import os
import pandas as pd
import requests

# read json file
with open('./urination.json', 'r') as data_file:
    json_data = data_file.read()
data = json.loads(json_data)["related_searches"]

# create DataFrame from json data
df = pd.DataFrame(data)

# create directory for query results
os.makedirs("results",exist_ok=True)

# extract query value
for idx, row in df.iterrows():

    query = row["query"] 
    url="https://api.serpwow.com/search"
    payload = {
        "api_key": "7B8A01FF4547497FA11B152D4400B2F9",
        "q": query,
        "engine": "google",
        "google_domain": "google.com"
    }
    result = requests.get(url,params=payload)
    print(result.json())
    with open(f"results/related_searches_{idx}.json","w") as file:
        json.dump(result.json(),file)

