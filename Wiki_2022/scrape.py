import pandas as pd
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup
import requests


def get_titles():
    '''
    Return pandas dataframe consisting of the titles of the articles present in the dataset
    '''
    articles = pd.read_csv('wikispeedia_paths-and-graph/articles.tsv', comment='#', delimiter='\t', encoding='utf8', names=['article']) 
    articles['article'] = articles['article'].apply(unquote)
    return articles

def title_from_link(link):
    '''
    Get wiki page title from its url
    '''
    try:
        rpos = link.rfind('/')
    except:
        return None
    else:
        return link[rpos+1:]

def get_links(soup, articles):
    '''
    Return all links found on a given page, for which we have an entry in the Wikispeedia dataset
    Parameters-
    soup: bs4 object of the webpage
    '''
    links = []
    for potential_link in soup.findAll('a'):
        link = potential_link.get('href')
        title = title_from_link(link)

        
        if title in articles.article.values:
            links.append(link)

    # Remove repitions
    links = list(set(links))
    print(len(links))

    return links

if __name__ == "__main__":
    articles = get_titles()
    base_url = "https://en.wikipedia.org/wiki/"
    for title in articles["article"].sample(5):
        url = base_url + title
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        outgoing_links = get_links(soup, articles)
        

