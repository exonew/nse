from nsepython import *
import json
from datetime import date
today_str = date.today().isoformat()
filename = f"data/{today_str}.json"
positions = nsefetch('https://www.nseindia.com/api/etf')
with open(filename, "w+") as f:
    json.dump(positions, f, indent=4)
print(f"Data saved to {filename}")
