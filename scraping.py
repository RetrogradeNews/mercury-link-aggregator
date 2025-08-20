import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Takes URL as input and returns time piece was published and piece's tags
def scrapeLinks(url):
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finds all hyperlinks on a webpage
    all_links = soup.find_all('a', href=True)

    # Finds links that lead to The Mercury
    links = []
    for link in all_links:
        href = link['href']
        
        # Parse the URL to get the domain
        parsed_url = urlparse(href)
        domain = parsed_url.netloc.lower()
        
        # Check if the domain contains 'target.com'
        if 'utdmercury.com' in domain:
            links.append(href)

    # Makes non-The Mercury linked pieces Null
    if links == []:
        links = None
    return links