from nsepython import *
import json
from datetime import date
import os

today_str = date.today().isoformat()
os.makedirs("data", exist_ok=True)
filename = f"data/{today_str}.json"
positions = nsefetch('https://www.nseindia.com/api/etf')
try:
    with open(filename, "w+") as f:
        json.dump(positions, f, indent=4)
    print(f"Data saved to {filename}")
