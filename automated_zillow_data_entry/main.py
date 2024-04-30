from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Goal of project: Automate data entry by finding the price, address, and links for places to rent in California
# that are up to 3k a month 1+ bed and 0+ bath by filling out a Google form.
# Note, this is a clone of Zillow that does not update...


url_form = "https://docs.google.com/forms/d/e/1FAIpQLSfQXEROlEys1iyPyJg6hGMLuFhHeGa9Ti3engoz2O1rVDrSpw/viewform?usp=sf_link"
url_zillow_clone = "https://appbrewery.github.io/Zillow-Clone"

# Request to Zillow Clone
zillow_request = requests.get(url_zillow_clone)


# ------------------------------------ Scraping the housing information. -------------------#
def get_housing_data():
    if zillow_request.status_code == 200:
        soup = BeautifulSoup(zillow_request.content, "html.parser")
        housing_information = soup.find_all("div", class_="StyledPropertyCardDataWrapper")
        # Finding the list of links in a list comprehension (not doing it for the rest as
        # I personally find it easier to read the for statement and understand the logic better.
        list_of_links = [info.find("a")["href"] for info in housing_information]
        # Finding the list of prices ($)
        list_of_prices = []
        for price_info in housing_information:
            prices_with_symbols = price_info.find("span", class_="PropertyCardWrapper__StyledPriceLine")
            prices_with_some_symbols = prices_with_symbols.text.split("+")[0]
            prices_without_symbols = prices_with_some_symbols.split("/")[0]
            list_of_prices.append(prices_without_symbols)

        list_of_addresses = []
        for address_info in housing_information:
            addresses = address_info.find("address")
            # Getting rid of the '|' in some of the addresses.
            address_text = addresses.text.replace("|", ",")
            # Get rid of whitespace as well.
            list_of_addresses.append(address_text.strip())
        return list_of_addresses, list_of_prices, list_of_links
    else:
        print("Error retrieving housing data!")
        print(zillow_request.status_code)
        return [], [], []


# ------------------------------------ Filling in the form. -------------------#


# Using Selenium to fill in form
def fill_in_form(list_of_addresses, list_of_prices, list_of_links):
    for n in range(len(list_of_links)):
        driver = webdriver.Chrome()
        driver.get(url_form)
        time.sleep(2)
        # Find the input fields and fill in the data
        address = driver.find_element(by=By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price = driver.find_element(by=By.XPATH,
                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link = driver.find_element(by=By.XPATH,
                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = driver.find_element(by=By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

        address.send_keys(list_of_addresses[n])
        price.send_keys(list_of_prices[n])
        link.send_keys(list_of_links[n])
        submit_button.click()

        driver.quit()


# Call the functions
list_of_addresses, list_of_prices, list_of_links = get_housing_data()
fill_in_form(list_of_addresses, list_of_prices, list_of_links)
