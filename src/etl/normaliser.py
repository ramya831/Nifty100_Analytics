def normalize_year(year):
    """
    Convert year values into standard format.
    """

    if year is None:
        return None

    year = str(year)

    year = year.replace("FY", "")
    year = year.strip()

    return int(year)


def normalize_ticker(ticker):
    """
    Clean stock ticker names.
    """

    if ticker is None:
        return None

    ticker = str(ticker)

    ticker = ticker.upper()
    ticker = ticker.strip()

    return ticker
def normalize_year(year):
    return int(str(year).replace(".0",""))

def normalize_ticker(ticker):
    return ticker.upper().strip()