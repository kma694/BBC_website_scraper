from bs4 import BeautifulSoup
import requests

url = 'http://www.bbc.co.uk/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('div', { 'class': 'gs-c-promo' })
for article in articles:
    print("ARTICLE")
    headline = article.find('h3')
    print('HEADLINE: ' + headline.text)
    summary = article.find('p')
    if summary:
        print('SUMMARY: ' + summary.text)
    link = article.find('a')
    print('LINK: ' + link['href'])
    
