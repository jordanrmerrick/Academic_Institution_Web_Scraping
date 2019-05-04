import datetime
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

from state_links import get_month_links

# TODO
#   Make functions more dynamic... allow variable entries for class_, id {}, and find_all(' ')
#   Allow exporting to .xlsx and .json
#   General optimization
"""
First set of web pages. In each of these there are individual pages for each month of the year.
Pages are pulled using the get_month_links function and added to a list which in this case is link_index.
"""
state_links = ["https://2009-2017.state.gov/r/pa/prs/ps/2009/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2010/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2011/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2012/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2013/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2014/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2015/index.htm",
               "https://2009-2017.state.gov/r/pa/prs/ps/2016/index.htm"]

keywords = ["Republic of Korea", "South Korea", "India", "Pakistan", "Bangladesh", "Maldives", "Afghanistan",
            "Sri Lanka", "China", "Japan", "Indo-Pacific", "Asia-Pacific", "ASEAN", "Tokyo", "Beijing", "Seoul",
            "New Delhi"]


# assign the list of links by month to link_index. There are 96 pages (12 months*8 years).


# pulling every press release from each month.

# call all lists
class ScraperMain:
    # global variables

    def __init__(self, links):
        self.links = links

    def find_articles(self):
        # call lists
        approved_final = []
        dates = []
        approved_initial = []
        data_collated = []
        url = {}
        url = set(url)
        # import initial links to each month from state_links.py
        link_index = get_month_links(self.links)

        # import current hour:minute:second for the .csv naming

        # initial for loop, importing the data from each month
        for sublist_month in link_index:
            ind_link = sublist_month[1]
            page = requests.get(ind_link)
            soup = BeautifulSoup(page.text, 'html.parser')
            date_first = soup.find_all(class_="date-display-single")
            dates.append(date_first)
            collection_first = soup.find(class_="l-wrap")
            collection = collection_first.find_all('a')

            # find the date in mm/dd/yy format and assign it as date_final
            flattened_list = [y for x in dates for y in x]

            # collect all data and combine it as a list in [title, date, link] format
            for data, j in zip(collection, flattened_list):
                date = re.match(r"<span class=\"date-display-single\">(.*)</span>", str(j))
                date_final = date.group(1)
                title = data.contents[0]
                link_start = "https://2009-2017.state.gov" + data.get('href')
                data_collated.append([title, date_final, link_start])

            # check each article to see whether or not it has any of the approved keywords in it.
            for sublist in data_collated:
                if any(word in sublist[0] for word in keywords):
                    approved_initial.append(sublist)

            for i in approved_initial:
                url.add(i[2])

            for j in url:
                for k in data_collated:
                    if j == k[2]:
                        if k in approved_final:
                            pass
                        else:
                            approved_final.append(k)

            dates.clear()
            flattened_list.clear()

        print("Web scraping completed, now removing duplicates.")
        # remove duplicate items.
        return approved_final

    def output_to_csv(self):
        final = self.find_articles()
        currentDT = datetime.datetime.now()
        time = currentDT.strftime("%H:%M:%S")
        df = pd.DataFrame(final)
        df.to_csv("output_{}.csv".format(time))


initialize = ScraperMain(state_links)

initialize.output_to_csv()