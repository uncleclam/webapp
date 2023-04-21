from datetime import datetime
import json
import pandas as pd


# read json file
with open('../urination.json', 'r') as data_file:
    json_data = data_file.read()
data = json.loads(json_data)["related_searches"]

# create DataFrame from json data
df=pd.DataFrame(data)

# add timestamp to DataFrame
now = datetime.now()
now_fmt = now.strftime("%Y-%m-%d")
df["timestamp"] = now_fmt

# write to csv
df.to_csv("../piss_table.csv")