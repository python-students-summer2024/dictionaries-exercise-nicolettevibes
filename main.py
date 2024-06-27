"""
A virtual cookie shop.
Do not modify this file.
"""

from pathlib import Path
import cookie_shop

# get data from the CSV file into a list
filepath = Path(
    "data/cookies.csv"
)  # create a file path in a way that is both Mac- and Windows- compatible
list_of_cookies = cookie_shop.bake_cookies(filepath)

# open the cookie shop with the cookies read from the file
# this must run the rest of the program as documented
cookie_shop.run_shop(list_of_cookies)

import cookie_shop_extra_credit

filepath = Path("data/cookies.csv")
cookies = cookie_shop_extra_credit.load_cookies(filepath)
nuts_allergy, gluten_allergy, diabetes = cookie_shop_extra_credit.welcome_message()
    
filtered_cookies = cookie_shop_extra_credit.filter_cookies(cookies, nuts_allergy == 'yes', gluten_allergy == 'yes', diabetes == 'yes')
cookie_shop_extra_credit.display_cookies(filtered_cookies)
order = cookie_shop_extra_credit.take_order(filtered_cookies)
    
cookie_shop_extra_credit.display_order_summary(order)