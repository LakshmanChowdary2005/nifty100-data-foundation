def normalize_year(year):
    """
    Convert year values like:
    2024
    "2024"
    "2024-25"

    into

    2024
    """

    if year is None:
        return None

    year = str(year).strip()

    try:
        return int(year[:4])
    except:
        return None


def normalize_ticker(ticker):
    """
    Examples

    tcs.ns
    INFY.bo
    reliance.ns

    becomes

    TCS
    INFY
    RELIANCE
    """

    if ticker is None:
        return None

    ticker = str(ticker).strip().upper()

    ticker = ticker.replace(".NS", "")
    ticker = ticker.replace(".BO", "")

    return ticker