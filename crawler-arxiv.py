import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import string

def browse(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    abstract = np.array([])
    title = np.array([])
    abstract_aim = np.array([])
    index_aim = np.array([])
    main_tag = soup.find('li', class_='arxiv-result')
    dic = np.array([])
    index = 1
    for li_tag in main_tag.next_siblings:
        if(li_tag == None or li_tag =='\n'):
            continue
        information = {'abstract':'0', 'title':'0','author':'0','year':'0','index':'0'}
        #get abstract
        abstract_tag = li_tag.find('span', class_='abstract-full has-text-grey-dark mathjax')
        abstract_txt = list(abstract_tag.strings)[0]
        information['abstract'] = abstract_txt
        #get title
        title_tag = li_tag.find('p', class_="title is-5 mathjax")
        title_txt = title_tag.string
        information['title'] = title_txt
        #get time
        time_tag = li_tag.find('p', class_="is-size-7")
        time_txt = time_tag.strings
        time_submite = list(time_txt)[1]
        information['year'] = time_submite
        #add index
        information['index'] = index
        index+=1
        dic = np.append(dic,information)
    return dic

def search(dic, abstract_aim):
    dic_aim = np.array([])
    for information in dic:
        found = False
        for abstract_aim_element in abstract_aim:
            if information['abstract'].find(abstract_aim_element) > 0 and found == False:
                dic_aim = np.append(dic_aim, information)
                found = True
    return dic_aim

url = "https://arxiv.org/search/?searchtype=author&query=Alicea%2C+J&abstracts=show&size=200&order=-announced_date_first"
abstract_aim = ['Majorana']
dic = browse(url)
dic_aim = search(dic,abstract_aim)
f = open("crawler-arxiv.csv",'wt',encoding = 'utf-8')
for information in dic_aim:
    print(information['index'],file = f)
    print(information['title'],file = f)
    print(information['year'],file = f)
f.close



