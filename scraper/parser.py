from bs4 import BeautifulSoup
import csv
import json

def parseHtmlContent(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    json_content = soup.find('script', type='application/ld+json').string.strip()
    parsed_content = json.loads(json_content)['@graph']
    review_list = []

    for element in parsed_content:
        if element['@type'] == 'Review':
            headline = element['headline']
            text = element['reviewBody']
            rating = element['reviewRating']['ratingValue']
            review_list.append({
                "headline": headline,
                "text": text,
                "rating": rating
            })

    return review_list


