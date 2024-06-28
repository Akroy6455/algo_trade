from maticalgos.historical import historical
import datetime
import pandas as pd

ma = historical("adarsh6455@gmail.com")
ma.login("832403")

# Define start and end dates
start_date = datetime.date(2018, 1, 15)
end_date = datetime.date(2018, 1, 31)

# Initialize an empty DataFrame to store all data
all_data = pd.DataFrame()

# Loop through each date
current_date = start_date
while current_date <= end_date:
    try:
        data = ma.get_data("banknifty", current_date)
        if not data.empty:
            # Add a date column to the DataFrame
            data['Date'] = current_date
            all_data = pd.concat([all_data, data], ignore_index=True)
            print(f"Data fetched for {current_date}")
        else:
            print(f"No data available for {current_date}")
    except Exception as e:
        print(f"Unable to fetch data for {current_date}: {str(e)}")
    
    current_date += datetime.timedelta(days=1)

# Save to CSV
filename = f'banknifty_data_{start_date}_to_{end_date}.csv'
all_data.to_csv(filename, index=False)
print(f"Data saved to {filename}")

# Print the first few rows and data info
print(all_data.head())
print(all_data.info())