import string

import requests as requests

from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
dom = 'https://www.nature.com'  # Why are you so solid?


def get_news_links(source_url):   # subLinks from main url with 'news' tags
    response = requests.get(source_url)
    match response.status_code:
        case 200:
            news_links_list = []
            soup = BeautifulSoup(response.content, 'html.parser')
            news_article_links = soup.find_all('span', {'class': 'c-meta__type'}, text="News")  # Only news tags
            for news_article in news_article_links:
                anchor = news_article.find_parent('article').find('a', {'data-track-action': 'view article'})
                news_links_list.append(anchor.get('href'))  # subLinks with tags news
            return news_links_list
        case _:
            return print(f'The URL returned {response.status_code}')


def links_content(links_list, domain):
    for path in list(links_list):
        r = requests.get(domain + path)
        match r.status_code:
            case 200:
                soup = BeautifulSoup(r.content, 'html.parser')
                title = soup.find('h1').text.strip(string.punctuation).replace(' ', '_')  # title as a file name
                # can raise an OS_error with wrong syntactics
                source_file = open(f'{title}.txt', 'wb')
                content = soup.find("div", {"class": "c-article-body"}).text.encode().rstrip()
                source_file.write(content)  # binary string
                source_file.close()
                print(f'{title}.txt  Success')
            case _:
                return print(f'The URL returned {r.status_code}')
    return print('All files are saved correctly')


get_news_links(url)
links_content(get_news_links(url), dom)
