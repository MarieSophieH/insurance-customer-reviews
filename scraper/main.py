from bs4 import BeautifulSoup
import pandas as pd
import json
import csv

file_path = '/Users/sophiehouben/insurance-customer-reviews/scraper/example-reviews.html'
filename = 'insurance_ratings.csv'

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

json_content = soup.find('script', type='application/ld+json').string.strip()
parsed_content = json.loads(json_content)['@graph']

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')

    writer.writerow(['Headline', 'Text', 'Rating'])

    for element in parsed_content:
        if element['@type'] == 'Review':
            headline = element['headline']
            text = element['reviewBody']
            rating = element['reviewRating']['ratingValue']
            writer.writerow([headline, text, rating])