thonimport requests
from bs4 import BeautifulSoup
import json
import logging
from .extractors.leboncoin_parser import parse_listing
from .outputs.exporter import export_data

logging.basicConfig(level=logging.INFO)

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching page {url}: {e}")
        return None

def scrape_listings(url):
    page_content = fetch_page(url)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        listings = soup.find_all('div', class_='list-item')
        data = [parse_listing(listing) for listing in listings]
        return data
    return []

def main():
    url = 'https://www.leboncoin.fr/annonces/offres/'
    listings_data = scrape_listings(url)
    if listings_data:
        export_data(listings_data, 'output.json')
    else:
        logging.info("No listings found.")

if __name__ == "__main__":
    main()