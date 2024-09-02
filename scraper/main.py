from bs4 import BeautifulSoup
import pandas as pd
import json

file_path = '/Users/sophiehouben/insurance-customer-reviews/scraper/example-reviews.html'

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

json_content = soup.find('script', type='application/ld+json').string.strip()
parsed_content = json.loads(json_content)['@graph']

for element in parsed_content:
    if element['@type'] == 'Review':
        print(element['reviewRating']['ratingValue'])
        print(element['headline'])
        print(element['reviewBody'])
        print("_____")