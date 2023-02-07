import requests
from bs4 import BeautifulSoup
import json

articles_list = []
unique_list = []


def bbc_rss():

    r = requests.get('http://feeds.bbci.co.uk/news/rss.xml')
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')

    for a in articles:
        title = a.find('title').text
        link = a.find('link').text
        published = a.find('pubDate').text

        article = {
            'title': title,
            'link': link,
            'published': published,
        }
        articles_list.append(article)
    return articles_list

 # using set to filter duplicate


def remove_duplicates(list_of_dicts):

    seen = set()
    for dict in list_of_dicts:
        t = tuple(dict.items())
        if t not in seen:
            unique_list.append(dict)
            seen.add(t)
    return unique_list


def bbcPageScraper():

    for item in unique_list:
        r = requests.get(item['link'])
        soup = BeautifulSoup(r.content, features='xml')
        paragraph = ""
        contents = soup.findAll("div", {"data-component": "text-block"})

        for content in contents:
            p = content.text
            paragraph += p
            paragraph.split()
        item.update({"content": paragraph})


def remove_empty_dicts(list_of_dicts):
    keys_to_check = ["title", "link", "published", "content"]
    return [d for d in list_of_dicts if all(d.get(k, "") != "" for k in keys_to_check)]


def executeScraping():
    print("executing Scraping....")
    bbc_rss()
    remove_duplicates(articles_list)
    bbcPageScraper()

    print("Scraping completed!")


executeScraping()

final_list = remove_empty_dicts(unique_list)
