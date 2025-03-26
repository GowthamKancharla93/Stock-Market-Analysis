# Stock-Market-Analysis
This project is about interpreting stock market data with NumPy, Pandas, and Matplotlib to find important insights and visualize trends. The data is in a CSV file and contains historical stock prices, from which date and closing prices are filtered out for analysis.


Project features of note:

Data Preprocessing: The data is cleaned by removing column headers and choosing specific fields.

Moving Averages: A 7-day and a 30-day moving average is computed using the convolution function provided by NumPy to detect short-term and long-term trends.

Price Change Analysis: The day-to-day percentage change in the stock price is calculated, picking out major declines (threshold = -3%).

Visualization: A graph of stock price trend is plotted using Matplotlib, wherein:

Stock prices are plotted as a blue line.

Green and red markers show daily price rises and falls, respectively.

Red circles are used to mark major declines for easy recognition.

Moving averages are plotted on top to indicate trend directions.
