def bbc_news():
      import bs4
      import requests
      import time
      import json
      import numpy as np
      url = "https://www.bbc.com/news"   

      response = requests.get(url)
      if response.status_code == 200:
          webpage = response.content
          final_list = []
          soup = bs4.BeautifulSoup(webpage, 'html.parser')
          mainPage = (soup.find_all('div', attrs = {"class":"gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m"}))
          news = {}
          date_ = []
          if len(mainPage) > 4 :
              iterator = 4
          else:
              iterator = len(mainPage)     

          for i in range(iterator):
              titles = mainPage[i].div.find('a')
              date_time = mainPage[i].find('ul')
              date_time = date_time.text.split('ago')
              for j in range(len(date_time[0])):
                  if date_time[0][j] == 'h':
                      ind = j
                      break
              date_.append(date_time[0][: ind+1]+' '+ date_time[1])
              print(date_)
              mat = mainPage[i].div.find('p')
              news[titles.text] = mat.text
          for key in news:
              for j in date_:
                  res = """
                        *{}*
                        {}
                        {} {}""".format(key, news[key], j[0][:2]+' ago', j[1])
                  (res)
                  date_.pop(0)
                  break


# def intercept():
#       import bs4
#       import requests
#       import time
#       import json
#       import numpy as np
#       url = "https://theintercept.com"   

#       response = requests.get(url)
#       if response.status_code == 200:
#           webpage = response.content
#           final_list = []
#           soup = bs4.BeautifulSoup(webpage, 'html.parser')
#           mainPage = (soup.find_all('a', attrs = {"class":"Homepage-HomepageTopStoriesPrimaryNode-container"})) 
#           news = {}
#           date_ = []
#           if len(mainPage) > 3:
#               iterator = 3
#           else:
#               iterator = len(mainPage) 
#           for i in range(iterator):
#               titles = mainPage[i].find('h3')
#               mat = mainPage[i].find('p')
#               news[titles.text] = mat.text   
#       for key in news:
#           res = """
#                 *{}*
#                 {}""".format(key, news[key])   
#           print(res) 
def indian_express():
      import bs4
      import requests
      import time
      import json
      import numpy as np
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
              news[titles] = mat
      for keys in news:
          for j in date_:
            res = """
                    *{}*
                    {}
                    {}""".format(keys[1:-1], news[keys], j)
            (res)
            date_.pop(0)
            break

bbc_news()