import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load data from CSV file
df = pd.read_csv('bnifty.csv')

# Preprocess data (e.g., fill missing values, normalize)
df = df.ffill().bfill()

# Separate date column
date = df['date']

# Select numerical columns
numerical_cols = df.select_dtypes(include=[np.number])

# Scale numerical columns
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(numerical_cols)

# Create new dataframe with scaled data and original date column
df_scaled = pd.DataFrame(scaled_data, columns=numerical_cols.columns)
df_scaled['date'] = date

# Create sequences
seq_length = 30
X, y = [], []
for i in range(len(df_scaled) - seq_length):
    X.append(df_scaled.iloc[i:i+seq_length].values)
    y.append(df_scaled.iloc[i+seq_length]['close'])

X = np.array(X)
y = np.array(y)

# Save the result in a different CSV file
result_df = pd.DataFrame({'X': X.tolist(), 'y': y})
result_df.to_csv('result.csv', index=False)