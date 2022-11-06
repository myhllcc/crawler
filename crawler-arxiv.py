import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import string

def browse(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    f = open("crawler_arxiv.csv",'wt',encoding = 'utf-8')
    abstract = np.array([])
    title = np.array([])
    abstract_aim = np.array([])
    index_aim = np.array([])
    main_tag = soup.find('li', class_='arxiv-result')
    dic = np.array([])
    for li_tag in main_tag.next_siblings:
        if(li_tag == None or li_tag =='\n'):
            continue
        information = {'abstract':'0', 'title':'0','author':'0','year':'0'}
        #get abstract
        abstract_tag = li_tag.find('span', class_='abstract-full has-text-grey-dark mathjax')
        abstract_txt = list(abstract_tag.strings)[0]
        information['abstract'] = abstract_txt
        #title
        title_tag = li_tag.find('p', class_="title is-5 mathjax")
        title_txt = title_tag.string
        information['title'] = title_txt

        dic = np.append(dic,information)
    f.close()
    return dic
        
url = "https://arxiv.org/search/?searchtype=author&query=Alicea%2C+J&abstracts=show&size=200&order=-announced_date_first"
dic = browse(url)
print(dic)



