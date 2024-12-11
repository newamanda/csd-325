#Amanda New
#CSD325-A311
#Module 9 
#
import requests

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
response = requests.get(url)

print(response.status_code)

#print(response.json())

import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

    
