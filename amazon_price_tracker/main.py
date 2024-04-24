import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("env.txt")

# Constants
TARGET_PRICE = 100
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
USER_AGENT = os.getenv("USER_AGENT")

headers = {
    "User-Agent": User_Agent,
    "Accept-Language": "en-US,en;q=0.9",
}


def scape_price_and_name():
    """Function: Scrapes data off Amazon:
    Returns: Product's price and Product's name"""
    url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        price_element = soup.select_one("span.aok-offscreen")
        # Splitting the rice cooker data, the index might vary for you...
        name_of_product_split = soup.select_one("#productTitle").text.split()[0:12]
        # Since it is in a list, I'm joining it together to form the full sentence without the commas.
        name_of_product = ' '.join(name_of_product_split)
        if price_element:
            price_text = price_element.text.strip()
            try:
                # The first [0] element is the $ symbol.
                price_without_currency = float(price_text.split("$")[1])
                return price_without_currency, name_of_product
            # Catches cases where the price element on Amazon does not match the logic above or is a 
            # non-floating number, such as a string or int.
            except (IndexError, ValueError):
                print("Price format not recognized")
                return None, None
        else:
            print("Price information not found.")
            return None, None
    else:
        print(f"Error: {response.status_code}")
        return None, None


def send_email(price, product_name):
    """Sends an email to the emails and passwords from the constants section above."""
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=MY_EMAIL, password=PASSWORD)
        message = f"Subject: Your target price was reached for {product_name}\n\n"
        message += f"The current price is ${price}\n"
        message += (f"Here's a link to make it easier: "
                    f"'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)


def main():
    price, product_name = scape_price_and_name()
    if price <= TARGET_PRICE:
        send_email(price, product_name)
    else:
        print("Unfortunately the price is too high. Come back again later.")


if __name__ == "__main__":
    main()
