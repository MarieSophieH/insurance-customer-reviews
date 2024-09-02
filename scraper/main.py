from bs4 import BeautifulSoup
import pandas as pd
import parser
import csv

file_path = '/Users/sophiehouben/insurance-customer-reviews/scraper/example-reviews.html'
filename = 'insurance_ratings.csv'

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

parsed_content = parser.parseHtmlContent(html_content)

with open('insurance_ratings.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')

    writer.writerow(['Headline', 'Text', 'Rating'])

    for element in parsed_content:
        headline = element['headline']
        text = element['text']
        rating = element['rating']
        writer.writerow([headline, text, rating])