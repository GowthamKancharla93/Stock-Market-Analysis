import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Stock_data.csv")  
df.columns = df.columns.str.strip()  
print("Available columns: ", df.columns)
df = df[['Date', 'Close']]
close_prices = df['Close'].values
dates = df['Date'].values
print("\nFirst 5 Dates:", dates[:5])
print("First 5 Close Prices:", close_prices[:5])
window_size_7 = 7
window_size_30 = 30
moving_avg_7 = np.convolve(close_prices, np.ones(window_size_7) / window_size_7, mode='valid')
moving_avg_30 = np.convolve(close_prices, np.ones(window_size_30) / window_size_30, mode='valid')
price_diff = np.diff(close_prices)
colors = np.where(price_diff >= 0, 'green', 'red')
pct_change = np.diff(close_prices) / close_prices[:-1] * 100
df_pct = df.iloc[1:].copy()
df_pct['Pct_Change'] = pct_change
df_pct['Close'] = close_prices[1:] 
print("\nFirst 5 Daily Percentage Changes:\n", df_pct.head())
drop_threshold = -3
significant_drops = df_pct[df_pct['Pct_Change'] <= drop_threshold]
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], close_prices, label="Stock Price", color='blue')
plt.scatter(df['Date'][1:], close_prices[1:], c=colors, label="Stock Trend", marker='o')
plt.scatter(significant_drops['Date'], significant_drops['Close'], color='red', label="Significant Drop", marker='o', s=100)
plt.plot(dates[window_size_7 - 1:], moving_avg_7, label="7-Day Moving Avg", color='red')
plt.plot(dates[window_size_30 - 1:], moving_avg_30, label="30-Day Moving Avg", color='green')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock Price Trend (Green: Up, Red: Down)')
plt.legend()
plt.xticks(rotation=60)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
