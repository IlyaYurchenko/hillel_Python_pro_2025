from bs4 import BeautifulSoup as bs
import requests

url = 'https://scipost.org/atom/publications/comp-ai'
response = requests.get(url)
soup = bs(response.text, 'lxml-xml')


entries = soup.find_all('entry')
for entry in entries:
    title = entry.find('title').text
    link = entry.find('link')['href']
    summary_tag = entry.find('summary').text
    summary = summary_tag.strip() if summary_tag else '-'

    print(f'Title: {title}')
    print(f'Link: {link}')
    print(f'Summary: {summary}')



file = open('feed.xml').read()
soup = bs(file, 'lxml-xml')

