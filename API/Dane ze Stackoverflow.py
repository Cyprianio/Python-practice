import requests
import json
import webbrowser
from datetime import datetime, timedelta

time = datetime.today() - timedelta(days =7)

params = {
    "fromdate" : int(time.timestamp()),
    "order" : "desc",
    "sort" : "votes",
    "tagged" : "python",
    "site" : "stackoverflow",
    "min" : 10
    }

r = requests.get("https://api.stackexchange.com/2.3/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONcodeError:
    print("Brak JSON na stronie")
else:
    for question in questions["items"]:
        webbrowser.open(question['link'])
        
