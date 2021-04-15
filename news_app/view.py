from django.shortcuts import render

# Create your views here.

import bs4
import requests
import time
import json
#import numpy as np
url = "https://www.bbc.com/news"   

response = requests.get(url)
if response.status_code == 200:
    webpage = response.content
    final_list = []
    soup = bs4.BeautifulSoup(webpage, 'html.parser')
    mainPage = (soup.find_all('div', attrs = {"class":"gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m"}))
    news = {}
    date_ = []
    if len(mainPage) > 4:
        iterator = 4
    else:
        iterator = len(mainPage)     
    ind = 0
    for i in range(iterator):
        titles = mainPage[i].div.find('h3')
        date_time = mainPage[i].find('ul')
        date_time = date_time.text.split('ago')
        for j in range(len(date_time[0])):
            if date_time[0][j] == 'h':
                ind = j
                break
        date_.append(date_time[0][: ind+1]+' '+ date_time[1])
        mat = mainPage[i].div.find('p')
        news[titles.text] = mat.text
list_1 = zip(news.items(), date_)

url = "https://indianexpress.com/section/india/"   

response = requests.get(url)
if response.status_code == 200:
    webpage = response.content
    final_list = []
    soup = bs4.BeautifulSoup(webpage, 'html.parser')
    mainPage = (soup.find_all('div', attrs = {"class":"articles"})) 
    news = {}
    date_ = []
    if len(mainPage) > 5:
        iterator = 5
    else:
        iterator = len(mainPage)  
    for i in range(iterator):
        titles = mainPage[i].h2.text
        mat = mainPage[i].p.text
        date_time = mainPage[i].find('div', attrs = {"class": "date"}).text
        date_.append(date_time)
        print(date_)
        news[titles[1:-1]] = mat
list_2 = zip(news.items(), date_)                 



def index(request):
    #return render(request, 'front/index.html', {}) 
    return render(request, 'front/index.html', {'bbc' : list_1, 'indian_express': list_2})
