import requests
import pandas as pd

# Your API key from aviationstack.com
API_KEY = '3182d951e7ae23f07d4fe699b0cddd52'

def fetch_flight_data():
    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&limit=100"

    response = requests.get(url)
    data = response.json()

    # Parse data into a DataFrame
    flights = []
    for item in data.get('data', []):
        try:
            flights.append({
                'Airline': item['airline']['name'],
                'From': item['departure']['airport'],
                'To': item['arrival']['airport'],
                'Departure Time': item['departure']['scheduled'],
                'Arrival Time': item['arrival']['scheduled']
            })
        except:
            continue

    df = pd.DataFrame(flights)
    df.to_csv('data.csv', index=False)
    print("Data saved to data.csv ✅")

# Run directly
if __name__ == "__main__":
    fetch_flight_data()
