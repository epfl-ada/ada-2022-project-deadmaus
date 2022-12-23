from bs4 import BeautifulSoup
f = open("2022/wpcd/wp/N/Nature.htm", "r")
soup = BeautifulSoup(f, "html.parser")
first_link = soup.a
# find all hrefs
print(first_link.find_all_next("a", href=True)[220].get('href'))

links = []

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

# for potential_link in soup.findAll('a'):
#     link = potential_link.get('href')
#     title = title_from_link(link)
#     links.append(title)

# # Remove repitions
# # links = list(set(links))
# print(links[:10])