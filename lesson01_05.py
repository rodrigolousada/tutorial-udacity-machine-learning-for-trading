from lesson01_02 import get_data
import pandas as pd
import matplotlib.pyplot as plt

def plot(df_data):
	ax=df_data.plot(title="Incomplete Data", fontsize=2)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()

def fill_missing_values(df_data):
    """Fill missing values in data frame, in place."""
    df_data.fillna(method="ffill", inplace=True)
    df_data.fillna(method="bfill", inplace=True)

if __name__ == '__main__':
    #list of symbols
    symbollist=["PSX", "FAKE1", "FAKE2"]
    #symbollist=["FAKE2"]
    #create date range
    dates=pd.date_range('2005-12-31','2014-12-07')
    #get adjusted close of each symbol
    df_data=get_data(symbollist,dates)

    # Fill missing values
    fill_missing_values(df_data)

    # Plot
    plot(df_data)
