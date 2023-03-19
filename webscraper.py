#Import Requests module
import requests
#Import BeautifulSoup 4
from bs4 import BeautifulSoup
#Import Pandas module
import pandas as pd

#Takes a URL, stores the input as a variable called response
url = input("Enter the URL of the URL you would like to scrape: ")
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href.startswith('https'):
        links.append(href)

data = []
for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else None
    data.append({'URL': link, 'Title': title})

df = pd.DataFrame(data)
print(df)