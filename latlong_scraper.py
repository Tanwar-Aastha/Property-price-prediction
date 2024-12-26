import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for Google Search
BASE_URL = "https://www.google.com/search?q="

# Headers to simulate a real browser visit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# Function to scrape latitude and longitude
def get_coordinates(sector):
    search_term = f"sector {sector} gurgaon longitude & latitude"
    response = requests.get(BASE_URL + search_term, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        coordinates_div = soup.find("div", class_="wvKXQ")
        if coordinates_div:
            return coordinates_div.text
    return None


# Create a DataFrame
df = pd.DataFrame(columns=["Sector", "Coordinates"])




# List to hold sector data as DataFrames
sectors_data = []

# Iterate over sectors and fetch coordinates (example for 1 to 10 sectors for testing)
for sector in range(1, 116):
    coordinates = get_coordinates(sector)
    sector_data = pd.DataFrame([{"Sector": f"Sector {sector}", "Coordinates": coordinates}])
    sectors_data.append(sector_data)

# Concatenate all individual sector DataFrames
df = pd.concat(sectors_data, ignore_index=True)
# Save DataFrame
df.to_csv("gurgaon_sectors_coordinates.csv", index=False)