import pandas as pd
import matplotlib.pyplot as plt

# Read CSV and Select Rows
def read_csv_basics():
    """
    df         --> prints entire dataframe
    df.head()  --> prints top 5 lines of the dataframe
    df.tail()  --> prints last 5 lines of the dataframe
    df.tail(n) --> prints last n lines of the dataframe
    df[10:21]  --> rows between 10 and 20
    """
    df = pd.read_csv("data/HCP.csv")
    print(df[10:21]) #rows between 10 and 20

# Compute max closing price
def get_max_close(symbol):
    """
    Return the maximum closing value for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) #read in data
    return df['Close'].max() #compute and return max

def get_max_close_run():
    """ Function called by Test Run. """
    for symbol in ['AAPL', 'IBM']:
        print("Max close")
        print(symbol, get_max_close(symbol))

# Compute mean volume
def get_mean_volume(symbol):
    """
    Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()

def get_mean_volume_run():
    """ Function called by Test Run. """
    for symbol in ['AAPL', 'IBM']:
        print("Mean Volume")
        print(symbol, get_mean_volume(symbol))

# Plotting stock price data
def plot_stock_price():
    """
    Stock price data printed inversely.
    """
    df = pd.read_csv("data/AAPL.csv")
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.show() # must be called to show plots

# Plot high prices for IBM
def plot_high_ibm():
    df = pd.read_csv("data/IBM.csv")
    df['High'].plot()
    plt.xlabel('Time')
    plt.ylabel('High prices')
    plt.title('High prices for IBM')
    plt.show()  # must be called to show plots

# Plot two columns
def plot_two_columns():
    df = pd.read_csv("data/AAPL.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show()

if __name__ == "__main__":
    # read_csv_basic()
    # get_max_close_run()
    # get_mean_volume_run()
    # plot_stock_price()
    # plot_high_ibm()
    plot_two_columns()
