import yfinance as yf


def get_stock_data(ticker: str):

    stock = yf.Ticker(ticker)

    hist = stock.history(period="1d")

    info = stock.info

    current_price = float(hist["Close"].iloc[-1])
    open_price = float(hist["Open"].iloc[0])

    price_change = current_price - open_price
    percent_change = (price_change / open_price) * 100

    return {
        "ticker": ticker,
        "current_price": current_price,
        "open_price": open_price,
        "price_change": round(price_change, 2),
        "percent_change": round(percent_change, 2),
        "volume": info.get("volume", "N/A"),
        "market_cap": info.get("marketCap", "N/A")
    }