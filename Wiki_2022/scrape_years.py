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



if __name__ == "__main__":
    st = time()
    articles = get_titles()
    # print(articles.head(2))
    articles_set = set(articles.article.values)
    site = pywikibot.Site("en", "wikipedia")
    links09 = pd.read_csv('wikispeedia_paths-and-graph/links.tsv', comment='#', delimiter='\t', names=['linkSource', 'linkTarget'])
    # print(next(x).revid)
    activ = 0
    checkpoint_article = "Frederick_II%2C_Holy_Roman_Emperor"
    checkpoint_year = 2010 # Make sure that there is at least one revision for that article for that year
    ctr = 0
    break_every = 5
    for article in tqdm(articles["article"]):
        coll = True
        if activ == 0 and article!=checkpoint_article:
            continue
        title = (unquote(article))
        ctr += 1
        rev_times = []
        req_times = []
        bs_times = []
        ln_times = []
        if ctr > break_every:
            print(article)
            break
            sleep(10)
            ctr = 0
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
                t1 = time()
                revs = pg.revisions(content=True, total=1, starttime=str(year)+"-01-01T00:00:00Z", endtime=str(year)+"-12-31T00:00:00Z", reverse=True)
                rev = next(revs)
                t2 = time()
                rev_times.append(t2-t1)
            except:
                cur_links = prev_links
            else:
                num += 1
                prev = revs
                old_id = rev.revid
                urls = url + "&oldid=" + str(old_id)
                try:
                    r_st = time()
                    page = requests.get(urls, timeout=5)
                    r_en = time()
                    req_times.append(r_en-r_st)
                except:
                    print(article, year)
                    coll = False
                    break
                else:
                    bs_st = time()
                    soup = BeautifulSoup(page.content, "html.parser")
                    bs_en = time()
                    bs_times.append(bs_en-bs_st)
                    ln_st = time()
                    outgoing_links = get_links(soup, articles_set) # order of links seems to be completely random
                    for ol in outgoing_links:
                        cur_links.append((article, ol))
                    ln_en = time()
                    ln_times.append(ln_en-ln_st)
                    prev_links = cur_links
            # print(len(cur_links))
            if coll:
                links = pd.DataFrame(cur_links, columns=['linkSource', 'linkTarget'])
                output_path = "Wiki_Revs/links"+str(year)[-2:]+".tsv"
                links.to_csv(output_path, sep="\t", index=False, mode='a', header=not os.path.exists(output_path))
            else:
                break
        if coll==False:
            break
        print("Time for getting revisions: ", sum(rev_times) / len(rev_times))
        print("Time for getting requests: ", sum(req_times) / len(req_times))
        print("Time for getting beautiful soup: ", sum(bs_times) / len(bs_times))
        print("Time for getting links: ", sum(ln_times) / len(ln_times))
        # if num < 12:
        #     print(num)
    en = time()
    print(en-st)
