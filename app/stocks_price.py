import finnhub

API_KEY = "cj1666hr01qjpc2n6mpgcj1666hr01qjpc2n6mq0"

finhub_client = finnhub.Client(api_key=API_KEY)


def get_stock_price(company_ticker: str):
    result = finhub_client.quote(company_ticker)
    # Error handling?
    return result["c"]


if __name__ == "__main__":
    print(get_stock_price("TSLA"))
