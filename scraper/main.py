from bs4 import BeautifulSoup
import pandas as pd
import parser
import csv
import requests

insurances = {
    'AOK': 'www.aok.de',
    'HUK': 'www.huk-coburg.de',
    'LV1871': 'www.lv1871.de',
    'Allianz': 'www.allianz.de' 
}

for insurance in insurances:

    insurance_url = insurances[insurance]
    url = 'https://www.trustpilot.com/review/' + insurance_url + '?languages=all'
    filename = 'ratings_' + insurance + '.csv'
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(['Headline', 'Text', 'Rating'])

        is_avalaible = True
        index = 1

        while(is_avalaible):
            request_url = url

            if index > 1:
                request_url += '&page=' + str(index)
                
            index += 1
            response = requests.get(request_url)

            if response.status_code == 200:
                html_content = response.text
                parsed_content = parser.parseHtmlContent(html_content)

                for element in parsed_content:
                    headline = element['headline']
                    text = element['text']
                    rating = element['rating']
                    writer.writerow([headline, text, rating])

            elif response.status_code == 404:
                is_avalaible = False
