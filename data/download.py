import pandas as pd
import yfinance as yf

def download_data(ticket: str) -> pd.DataFrame:
    """download data from source

    Args:
        ticket (str): the ticket of the financial asset you want to download

    Returns:
        pd.DataFrame: a dataframe for the given ticket
    """
    data = yf.download(ticket)
    return data

 