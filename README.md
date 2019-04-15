Dependencies:

- state_links
- pandas
- re
- bs4 (BeautifulSoup)
- requests

This program is designed to scrape all relevant press releases from the State Department.

It utilizes BeautifulSoup, re, requests, and pandas.

The parameters needed to run this file are:
1. A list of keywords. The program distinguishes which articles are relevant
    by the keywords in the title.
    
2. The state department websites. Currently the program looks at all press releases
    from 2009 to 2016, though you can add current releases or look at archived
    releases from before 2009. This can be edited under the state_links list in 'state_links.py'
    
3. The name of the csv file you want to output the results to. This is called as a string.

Enter them in the 'main.py' file. 'main.py' is dependent on 'state_links.py'

'state_links.py' collects all the links for every month from 2009 to 2016.
You can change the website links to search in the state_links list.

