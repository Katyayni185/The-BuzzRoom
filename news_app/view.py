from django.shortcuts import render

# Create your views here.
def bbc_news():
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
          if len(mainPage) > 5:
              iterator = 5
          else:
              iterator = len(mainPage)     

          for i in range(iterator):
              titles = mainPage[i].div.find('a')
              date_time = mainPage[i].find('ul')
              date_.append(date_time.text.split('ago'))
              mat = mainPage[i].div.find('p')
              news[titles.text] = mat.text
          for key in news:
              for j in date_:
                  res = """
                        *{}*
                        {}
                        {} {}""".format(key, news[key], j[0][:2]+' ago', j[1])
                  print(res)
                  date_.pop(0)
                  break
                  
bbc_news()


def index(request):
    #return render(request, 'front/index.html', {}) 
    return render(request, 'front/index.html', {bbc_news()}) 
