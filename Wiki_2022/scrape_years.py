import pandas as pd
from urllib.parse import quote, unquote
import pywikibot
from itertools import islice
from time import time
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from  scrape import get_links, get_titles, title_from_link
import os



if __name__ == "__main__":
    st = time()
    articles = get_titles()
    # print(articles.head(2))
    articles_set = set(articles.article.values)
    site = pywikibot.Site("en", "wikipedia")
    links09 = pd.read_csv('wikispeedia_paths-and-graph/links.tsv', comment='#', delimiter='\t', names=['linkSource', 'linkTarget'])
    # print(next(x).revid)
    activ = 0
    checkpoint_article = "Crash_test_dummy"
    checkpoint_year = 2016 # Make sure that there is at least one revision for that article for that year
    for article in tqdm(articles["article"]):
        if activ == 0 and article!=checkpoint_article:
            continue
        title = (unquote(article))
        prev_links = list(links09[links09["linkSource"] == article].itertuples(index=False, name=None)) # link structure from the wikispeedia dataset
        base_url = "https://en.wikipedia.org/w/index.php?"
        url = base_url + title
        pg = pywikibot.Page(site, article)
        num = 0
        for year in range(2010, 2022):
            if activ == 0:
                if year < checkpoint_year:
                    continue
                else:
                    activ = 1
            cur_links = [] # list of tuples (source, target) for current year and current article
            try:
                revs = pg.revisions(content=True, total=1, starttime=str(year)+"-01-01T00:00:00Z", endtime=str(year)+"-12-31T00:00:00Z", reverse=True)
                rev = next(revs)
            except:
                cur_links = prev_links
            else:
                num += 1
                prev = revs
                old_id = rev.revid
                urls = url + "&oldid=" + str(old_id)
                page = requests.get(urls)
                soup = BeautifulSoup(page.content, "html.parser")
                outgoing_links = get_links(soup, articles_set) # order of links seems to be completely random
                for ol in outgoing_links:
                    cur_links.append((article, ol))
                prev_links = cur_links
            # print(len(cur_links))
            links = pd.DataFrame(cur_links, columns=['linkSource', 'linkTarget'])
            output_path = "Wiki_Revs/links"+str(year)[-2:]+".tsv"
            links.to_csv(output_path, sep="\t", index=False, mode='a', header=not os.path.exists(output_path))
        if num < 12:
            print(num)
    en = time()
    print(en-st)
