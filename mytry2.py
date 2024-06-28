import numpy as np
from typing import List

import csv

def csv_to_int_list(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        # Remove brackets, convert to integer
        return [float(item[0].strip('[]')) for item in csv_reader]

# Assign the result to a variable
my_data = csv_to_int_list('niftynidhi.csv')
current = csv_to_int_list('current.csv')

def convert_to_binary(candles: List[float]) -> List[int]:
    binary = [0]  # First candle is always 0 as there's no previous candle
    for i in range(1, len(candles)):
        binary.append(1 if candles[i] > candles[i-1] else 0)
    return binary

def predict_next_15_minutes(historical_data: List[float], current_data: List[float]) -> str:
    # Convert historical and current data to binary
    historical_binary = convert_to_binary(historical_data)
    current_binary = convert_to_binary(current_data)[-375:]  # Get last 375 candles

    up_points = 0
    down_points = 0

    # Calculate weights
    weights = [0.999 ** i for i in range(len(historical_binary) - 375 - 15)][::-1]

    # Compare current 375 candles with every 375-candle sequence in historical data
    for i in range(len(historical_binary) - 375 - 15):
        historical_sequence = historical_binary[i:i+375]
        next_15_candles = historical_binary[i+375:i+390]  # Next 15 candles

        # Calculate point for this sequence
        point = sum([1 if h == c else -1 for h, c in zip(historical_sequence, current_binary)])

        # Apply weight to the point
        weighted_point = abs(point) * weights[i]

        # Evaluate the trend in the next 15 candles
        up_count = sum(next_15_candles)
        down_count = 15 - up_count

        # Add weighted point to up or down based on the majority trend in next 15 candles
        if up_count > down_count:
            up_points += weighted_point
        elif down_count > up_count:
            down_points += weighted_point
        # If equal, we don't add points to either direction

    # Calculate total points and ratio
    total_points = up_points + down_points
    ratio = (up_points / total_points) if total_points > 0 else 0.5

    # Determine prediction
    if up_points > down_points:
        direction = "UP"
    elif down_points > up_points:
        direction = "DOWN"
    else:
        direction = "NEUTRAL"

    return f"{direction} (Ratio: {ratio:.4f}, Up points: {up_points:.2f}, Down points: {down_points:.2f})"

# Example usage
# Note: You'll need to provide much larger datasets for both historical and current data
historical_data = my_data # Repeated to create a larger dataset
current_data = current  # Repeated to create 380 data points

prediction = predict_next_15_minutes(historical_data, current_data)
print(f"Prediction for next 15 minutes: {prediction}")