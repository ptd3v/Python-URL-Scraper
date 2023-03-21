# Python URL Scraper
To use this script, simply run it and enter the URL of the web page you want to scrape.
The script will then scrape all the links on the page and return a Pandas data frame with the URL and title of each link.

Note: The URL must contain 'http://'. (Fixed 0.5)

Required Modules:
Requests,
BeautifulSoup4,
Pandas

Known issues:
Cannot add the full URL to internal links. (Fixed 0.4)
URL's without 'http://' throw an error. (Fixed 0.5)