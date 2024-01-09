"""
The code below is used to scrape the UFC website for the fight card of a given UFC event.
The code is used to scrape the HTML of the UFC website and then parse the HTML using BeautifulSoup.

You can view the current output and find the data, it is mostly organized in a table.
You might need to search through the HTML entirely to find how the data is organized.
"""

from bs4 import BeautifulSoup
import requests

def print_elements(ufc_card):
    with open(f"./ufc{ufc_card}.txt", "r") as file:
        html = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Print out the HTML
    print(soup.prettify())

    # Print out the table contents
    table = soup.find("table")
    print("\n\n", table)

    # Print out the table rows
    table_rows = table.find_all("tr")
    print("\n\n", table_rows)

    # Print out the table headers
    table_headers = table_rows[0].find_all("th")
    print("\n\n", table_headers)

    # Print out the table data
    table_data = table_rows[1].find_all("td")
    print("\n\n", table_data)


# Example usage
ufc_card = "294"
print_elements(ufc_card)