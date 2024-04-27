import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Possibly a way to get the script running faster in check find all elements in the menu
# Make them into separate buttons locally. Also, bot breaks when I get to 1000. Maybe I'll come back to
# this project...

# So I call this, early game cookie clicker bot!


# Constants 


CLICKER = 0  # Number of clicks the program does
NUM_TO_WAIT_IN_COOKIES = 50  # How 'time' is calculated in the program.


# Setting up Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Various elements grabbed from the cookie clicker game.

cookie_button = driver.find_element(By.ID, "cookie")
buycursor_button = driver.find_element(By.ID, "buyCursor")
buy_grandma = driver.find_element(By.ID, "buyGrandma")
money = driver.find_element(By.ID, "money")
cookies_per_second = driver.find_element(By.ID, "cps")
buy_factory = driver.find_element(By.ID, "buyFactory")

# ---------------------------------- Calculating best upgrade-------------#


def calculate_best_upgrade(money, upgrade_costs):
    """Calculates the best upgrade by determining if we have enough cookies. It takes the
    cps_increase to the if statement below it. If the cps_increase is greater than the
    max_cps_increase it will replace the best_upgrade or else it will save up cookies for future upgrades."""
    best_upgrade = None
    max_cps_increase = 0

    for upgrade, cost in upgrade_costs.items():
        if money >= cost:
            cps_increase = 0
            if upgrade == "Cursor":
                cps_increase = 0.2
            elif upgrade == "Grandma":
                cps_increase = 1.4
            elif upgrade == "Factory":
                cps_increase = 4.0
            # Add more upgrade types here

            if cps_increase / cost > max_cps_increase:
                max_cps_increase = cps_increase / cost
                best_upgrade = upgrade

    return best_upgrade


upgrade_costs = {
    "Cursor": 15,
    "Grandma": 100,
    "Factory": 500,
    # Add more upgrade types and costs here
}

# ---------------------------------- Main -------------#
while CLICKER <= 5000:
    try:
        cookie_button.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        # Refresh the element reference
        cookie_button = driver.find_element(By.ID, "cookie")
        cookie_button.click()
    CLICKER += 1

    if CLICKER % NUM_TO_WAIT_IN_COOKIES == 0:
        time.sleep(1)
        # For debugging and visualing...
        print("Thinking...")
        print(upgrade_costs["Cursor"])
        print(upgrade_costs["Grandma"])
        print(upgrade_costs["Factory"])
        try:
            current_money = int(money.text)
            current_cps = float(cookies_per_second.text.split(" ")[2])
            best_upgrade = calculate_best_upgrade(current_money, upgrade_costs)
            print(current_cps)

            if best_upgrade:
                print(f"Bought {best_upgrade}")
                upgrade_element = driver.find_element(By.ID, f"buy{best_upgrade}")
                upgrade_element.click()
                # Increasing to give a longer buffer time before each new use.
                NUM_TO_WAIT_IN_COOKIES += 2

                # Increase upgrade after every purchase
                upgrade_costs_multiplier = int((upgrade_costs[best_upgrade] * 0.15))
                upgrade_costs[best_upgrade] += upgrade_costs_multiplier
            else:
                print("Not enough money for any upgrades/saving cookies.")
        except selenium.common.exceptions.StaleElementReferenceException:
            # Refresh the element references
            money = driver.find_element(By.ID, "money")
            cookies_per_second = driver.find_element(By.ID, "cps")
