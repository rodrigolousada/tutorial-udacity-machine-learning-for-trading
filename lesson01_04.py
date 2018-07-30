from lesson01_02 import get_data, plot_data
import pandas as pd
import matplotlib.pyplot as plt

def compute_statistics():
    # Read data
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY','XOM','GOOG','GLD']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute global statistics for each stock
    print(df.mean())
    print(df.median())
    print(df.std())

def rolling_mean():
    # Read data
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    # Compute rolling mean using a 20-day window
    # deprecated -> rm_SPY = pd.rolling_mean(df['SPY'], window=20)
    rm_SPY = df['SPY'].rolling(window=20, center=False).mean()

    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    # Add acis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc = 'upper left')
    plt.show()


#9. Quiz -> Bollinger Bands.
def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    # deprecated -> pd.rolling_mean(values, window=window)
    return values.rolling(window=window, center=False).mean()

def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    # deprecated -> pd.rolling_std(values, window=window)
    return values.rolling(window=window, center=False).std()

def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    upper_band = rm + 2*rstd
    lower_band = rm - 2*rstd
    return upper_band, lower_band


def bollinger_bands():
    """Bollinger Bands."""
    # Read data
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], window=20)

    # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df['SPY'], window=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

#11. Quiz -> Compute daily returns
def compute_daily_returns(df):
    """Compute and return the daily return values."""

    # Using numpy:
    # daily_returns = df.copy() #copy given DataFrame to match size and column names
    # # compute daily return for row 1 onwards
    # daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    # daily_returns.ix[0,:] = 0 # set daily return for row 0 to 0

    # Using Pandas dataframe function
    daily_returns = (df / df.shift(1)) - 1 # much easier with Pandas!
    daily_returns.ix[0,:] = 0 # Pandas leaves the 0th row full of NaNs
    return daily_returns

def compute_daily_returns_run():
    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-31')  # one month only
    symbols = ['SPY','XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

#12. -> Compute cumulative returns
def compute_cumulative_returns(df):
    """Compute and return the cumulative return values."""
    cumulative_returns = (df / df.ix[0]) - 1
    return cumulative_returns

def compute_cumulative_returns_run():
    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-31')  # one month only
    symbols = ['SPY','XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute cumulative returns
    cumulative_returns = compute_cumulative_returns(df)
    plot_data(cumulative_returns, title="Cumulative returns", ylabel="Cumulative returns")


if __name__ == "__main__":
    # compute_statistics()
    # rolling_mean()
    # bollinger_bands()
    # compute_daily_returns_run()
    compute_cumulative_returns_run()
