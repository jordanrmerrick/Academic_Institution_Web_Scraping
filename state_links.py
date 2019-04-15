import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

state_links = ["https://2009-2017.state.gov/r/pa/prs/ps/2009/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2010/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2011/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2012/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2013/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2014/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2015/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2016/index.htm"]

data_collated = []
def get_month_links(link_list):
    for link in link_list:
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')

        collection_first = soup.find(class_="menu")
        collection = collection_first.find_all('a')

        for data in collection:
            link_initial = data.get('href')
            link = "https://" + link_initial[2:]
            title = data.contents[0]
            data_collated.append([title, link])

    return data_collated