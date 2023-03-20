# Python URL Scraper
To use this script, simply run it and enter the URL of the web page you want to scrape.
The script will then scrape all the links on the page and return a Pandas data frame with the URL and title of each link.

Note: The URL must contain 'http://'.

Required Modules:
Requests
BeautifulSoup4
Pandas

Known issues:
URL's without 'http://' throw an error.