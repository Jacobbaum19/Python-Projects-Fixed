import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv('env.txt')

# Various keys loaded from a separate file and the stocks name and company.
STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
my_email = os.getenv('my_email')
password = os.getenv("password")
STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# Grabbing Apple's stock information.
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCKS_API_KEY
}

r = requests.get(url=STOCK_ENDPOINT, params=parameters)
r.raise_for_status()

# Grabbing the last two day's closing price date.
data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
print(data_list)
yesterday_date = data_list[0]
day_before_yesterday_date = data_list[1]

# Last two day's closing price.
latest_closing_price = float(yesterday_date["4. close"])
second_latest_closing_price = float(day_before_yesterday_date["4. close"])


# Difference of closing prices calculation.

difference_of_closing_prices = latest_closing_price - second_latest_closing_price
print(difference_of_closing_prices)
# Percent change in closing prices
percent_change_in_closing_prices = round((difference_of_closing_prices / second_latest_closing_price) * 100, 2)
print(percent_change_in_closing_prices)


# Main logic to send the email.
if abs(percent_change_in_closing_prices) > 0.5:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "popularity",
        "pageSize": 3  # Limit to the first 3 articles
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][:3]
    articles_combined = [f"Headline: {article['title']}\nDesc: {article['description']}\nURL: {article['url']}\n"
                         for article in articles]

    # Combining the articles into a single string, properly formatted.
    articles_combined_str = "\n".join(articles_combined)

    # Preparing the email message with the appropriate headers
    msg = f"Subject: Stock Alert for {COMPANY_NAME}\n"
    # Using only the UTF-8 character encoding
    msg += "Content-Type: text/plain; charset=utf-8\n\n"
    msg += f"{COMPANY_NAME}: {percent_change_in_closing_prices}%\n\n"
    msg += articles_combined_str

    # Encoding the message as UTF-8 before sending
    msg_encoded = msg.encode('utf-8')

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="Jacobbaum19@gmail.com",
            msg=msg_encoded)
