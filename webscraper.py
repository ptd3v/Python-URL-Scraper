#Import Requests, BeautifulSoup 4 and Pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

#Takes a URL, stores the input as a variable called response. Loads the bs4 html parser.
url = input("Please enter the address of the URL you would like to scrape: ")
if not url.startswith("http"):
    url = "http://" + url

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# create an empty list to store the links and titles
url_and_titles = []

# Finds all links on the page and extracts their URLs/ titles. Appends to the empty list.
# Finds all links on the page and extracts their URLs/ titles. Appends to the empty list.
for link in soup.find_all("a"):
    href = link.get("href")
    if href.startswith("/"):
        href = urljoin(url, href)
    title = link.get("title") or link.text.strip()
    url_and_titles.append({"URL": href, "title": title})

#Saves the results as a dataframe, prints the results in the console and exports it as a csv.
result = pd.DataFrame(url_and_titles)
result.to_csv("urls_and_titles.csv", index=False)
print(result)