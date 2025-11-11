thonimport json
import re

def parse_listing(listing):
    data = {
        'list_id': extract_list_id(listing),
        'first_publication_date': extract_publication_date(listing),
        'index_date': extract_index_date(listing),
        'status': extract_status(listing),
        'category_id': extract_category_id(listing),
        'phone': extract_phone(listing),
        'original_phone': extract_original_phone(listing),
        'subject': extract_subject(listing),
        'body': extract_body(listing),
        'price': extract_price(listing),
        'location': extract_location(listing),
        'images': extract_images(listing),
    }
    return data

def extract_list_id(listing):
    # Dummy extraction function
    return listing.get('data-id')

def extract_publication_date(listing):
    # Dummy extraction function
    return listing.get('data-pub-date')

def extract_index_date(listing):
    # Dummy extraction function
    return "2025-04-24 08:43:25"

def extract_status(listing):
    # Dummy extraction function
    return "active"

def extract_category_id(listing):
    # Dummy extraction function
    return listing.get('data-category-id')

def extract_phone(listing):
    # Dummy extraction function
    return "02996*****"

def extract_original_phone(listing):
    # Dummy extraction function
    return ""

def extract_subject(listing):
    # Dummy extraction function
    return listing.find('h2').text

def extract_body(listing):
    # Dummy extraction function
    return listing.find('p', class_='description').text

def extract_price(listing):
    # Dummy extraction function
    price_text = listing.find('span', class_='price').text
    return [float(re.sub(r'[^0-9.]', '', price_text))]

def extract_location(listing):
    # Dummy extraction function
    return listing.find('span', class_='location').text

def extract_images(listing):
    # Dummy extraction function
    images = listing.find_all('img')
    return [img['src'] for img in images]