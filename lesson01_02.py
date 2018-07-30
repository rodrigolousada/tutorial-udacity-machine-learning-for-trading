''' Build a dataframe in pandas '''
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""

    # # Slice by row range (dates) using DataFrame.ix[] selector
    # print(df.ix['2010-01-01':'2010-01-31']) # the month of January
    #
    # # Slice by columns (symbols)
    # print(df['GOOG']) # a single label selects a sngle column
    # print(df[['IBM','GLD']]) # a list of labels selects multiple columns
    #
    # # Slice by row and column
    # print(df.ix['2010-03-01':'2010-03-15', ['SPY','IBM']])

    plot_data(df.ix[start_index:end_index, columns], title="Selected data")

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    # Create an empty DataFrame
    df = pd.DataFrame(index=dates)

    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    # Read in selected stocks
    for symbol in symbols:
        # Read symbol data into temporary DataFrame
        # Date as index of the table
        # Dates still appear in the set
        # Only extract 'Date' and 'Adj Close' columns
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date",
                            parse_dates=True, usecols = ['Date', 'Adj Close'],
                            na_values=['nan'])

        # rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        df = df.join(df_temp) #use default how='left'
        if symbol == 'SPY': #drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df

def normalize_data(df):
    """Normalize stock prices using the first row of the dataframe."""
    return df / df.ix[0,:]

def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show() # must be called to show plots in some environments

def dataframe_builder():
    # Define a date range
    start_date = '2010-01-01'
    end_date = '2010-12-31'
    dates = pd.date_range(start_date,end_date)

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    # Slice and plot
    # plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')

    plot_data(normalize_data(df))

if __name__ == "__main__":
    dataframe_builder()


# Unused now, but valuable information:
# Two ways of joining dataframes using Dataframe.join()
# [1]
# df1 = df1.join(dfSPY) #default how='left'
# df1 =df1.dropna()
#
# [2]
# df1 = df1.join(dfSPY, how='inner')
