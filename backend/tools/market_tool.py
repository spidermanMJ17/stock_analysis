import yfinance as yf


def get_stock_data(ticker: str):

    stock = yf.Ticker(ticker)

    hist = stock.history(period="1d")

    current_price = float(hist["Close"].iloc[-1])
    open_price = float(hist["Open"].iloc[0])

    price_change = current_price - open_price

    return {
        "ticker": ticker,
        "current_price": current_price,
        "price_change": price_change
    }