import requests
from bs4 import BeautifulSoup


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