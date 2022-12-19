import pandas as pd
from urllib.parse import quote, unquote
import pywikibot
from itertools import islice
from time import time, sleep
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from  scrape import get_links, get_titles, title_from_link
import os
import multiprocessing
from functools import partial

def f(art , num):
    title = unquote(art)
    return title, num


if __name__ == "__main__":
    pool = multiprocessing.Pool(16)
    articles = get_titles().article.to_list()
    print(articles[:16])
    for x in pool.imap_unordered(partial(f, num=1), articles[:16]):
        print(x)