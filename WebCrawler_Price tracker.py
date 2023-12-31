from bs4 import BeautifulSoup # library for pulling data out of HTML and XML files #
import requests # send HTTP/1.1 requests #
import numpy as np # operations on arrays #
import csv
from datetime import datetime

LINK = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=dell+workstation&_sacat=175672&_udlo=350&_udhi=750&LH_ItemCondition=1500&rt=nc&LH_BIN=1"

def get_prices_by_link(link):
    # get source
    r = requests.get(link)
    # parse source
    page_parse = BeautifulSoup(r.text, 'html.parser')
    # find all list items from search results
    search_results = page_parse.find("ul",{"class":"srp-results"}).find_all("li",{"class":"s-item"})

    item_prices = []

    for result in search_results:
        price_as_text = result.find("span",{"class":"s-item__price"}).text
        # avoid prices "from $x to $y"
        if "to" in price_as_text:
            continue
        # remove first index $ £ €
        price = float(price_as_text[1:].replace(",",""))
        item_prices.append(price)
    return item_prices

def remove_outliers(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def get_average(prices):
    return np.mean(prices)

def save_to_file(prices):
    fields=[datetime.today().strftime("%B-%D-%Y"),np.around(get_average(prices),2)]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

if __name__ == "__main__":
    prices = get_prices_by_link(LINK)
    prices_without_outliers = remove_outliers(prices)
    print("Average price: ", get_average(prices_without_outliers))
    print("Minimal price: ", np.min(prices_without_outliers))
    save_to_file(prices)
