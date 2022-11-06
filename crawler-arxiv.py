import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import string


page = requests.get("https://arxiv.org/search/cond-mat?query=Alicea%2C+J&searchtype=author&abstracts=show&order=-announced_date_first&size=50")
soup = BeautifulSoup(page.content,'html.parser')
f = open("crawler_arxiv.csv",'wt',encoding = 'utf-8')
first_tag = soup.find_all('span', class_='abstract-full has-text-grey-dark mathjax') 
abstract = np.array([])
title = np.array([])
abstract_aim = np.array([])
index_aim = np.array([])
for sub_tag in first_tag:
    abstract_txt = list(sub_tag.strings)[0]
    #Because the sub_tag contains multiple string. the zeroth one is what we want
    abstract = np.append(abstract, abstract_txt)
searching_text = 'Majorana'

#find title 
title_tag = soup.find_all('p', class_ = "title is-5 mathjax")
for sub_tab in title_tag:
    title_txt = sub_tab.string
    title = np.append(title, title_txt)
#get the aim title 
for index, line in enumerate(abstract):
    if line.find(searching_text) > 0:
        title_aim = title[index]
        print(title_aim,file = f)
        print(index,file = f)
        #print(index,file = f)
f.close()
