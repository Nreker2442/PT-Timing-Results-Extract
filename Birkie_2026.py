import requests
import pandas as pd

url = "https://my4.raceresult.com/380971/RRPublish/data/list"

params = {
    "key": "165f512b9755baa4f95b188a873c4739",
    "listname": "Result Lists|Overall Results",
    "page": "results",
    "contest": 10,
    "r": "leaders",
    "l": 4000,              # increase limit to cover all results
    "openedGroups": "{}",
    "term": ""
}

resp = requests.get(url, params=params)
data = resp.json()

# Extract raw rows
raw_rows = data["data"]["#1_Birkebeiner Skate"]

# Filter out summary rows
rows = [r for r in raw_rows if len(r) > 1]

# Get field labels
columns = data["DataFields"]

# Make a DataFrame
df = pd.DataFrame(rows, columns=columns)

print(df.head())
print(f"\nTotal rows: {len(df)}")

# Optional: save as CSV
df.to_csv(r"<file_path>", index=False)
