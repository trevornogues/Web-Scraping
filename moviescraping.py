from requests import get
from bs4 import BeautifulSoup


url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = get(url)
# print(response.text[:500])



html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)



movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
# print(type(movie_containers))
# print(len(movie_containers))



#Find first movie name and year:
first_movie = movie_containers[0]
first_movie
first_name = first_movie.h3.a.text
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
first_year = first_year.text
#print(first_name, first_year) 

#Find IMDB and Metascore scores:
first_imdb = float(first_movie.strong.text)
first_mscore = first_movie.find('span', class_ = 'metascore favorable')
first_mscore = int(first_mscore.text)
#print(first_imdb, first_mscore)

#Find number of votes:
first_votes = first_movie.find('span', attrs = {'name':'nv'})
first_votes = int(first_votes['data-value'])
#print(first_votes)

'''
#Scrape entire page for desired data:

names = []
years = []
imdb_ratings = []
metascores = []
votes = []

#Extract data from individual movie container
for container in movie_containers:

    # If the movie has Metascore, then extract:
    if container.find('div', class_ = 'ratings-metascore') is not None:

        # The name
        name = container.h3.a.text
        names.append(name)

        # The year
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)

        # The IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        # The Metascore
        m_score = container.find('span', class_ = 'metascore').text
        metascores.append(int(m_score))

        # The number of votes
        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))

'''
'''
import pandas as pd
#Check that scraping worked:
test_df = pd.DataFrame({'movie': names,
                       'year': years,
                       'imdb': imdb_ratings,
                       'metascore': metascores,
                       'votes': votes})
print(test_df.info())
'''

headers = {"Accept-Language": "en-US, en;q=0.5"}

from time import sleep
from random import randint

pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2000,2018)]


#Checks frequency of requests.
from time import time
from IPython.core.display import clear_output
from warnings import warn

start_time = time()
requests = 0

"""
for _ in range(5):
    # A request would go here
    requests += 1
    sleep(randint(1,3))
    current_time = time()
    elapsed_time = current_time - start_time
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)

warn("Warning Simulation")
"""

#Putting it all together:
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

start_time = time()
requests = 0

for year_url in years_url:
        for page in pages:
                response = get('http://www.imdb.com/search/title?release_date=' + year_url + 
                                '&sort=num_votes,desc&page=' + page, headers = headers)

                sleep(randint(8,15))

                requests += 1
                elapsed_time = time() - start_time
                print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
                clear_output(wait = True)

                if response.status_code != 200:
                        warn('Request: {}; Status code: {}'.format(requests, response.status_code))
                        break
                
                if requests > 50:
                        warn('Number of requests was greater than expected.')  
                        break 
                
                page_html =  BeautifulSoup(response.text, 'html.parser')

                mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

                for container in mv_containers:
                        if container.find('div', class_ = 'ratings-metascore') is not None:
                                name = container.h3.a.text
                                names.append(name)

                                year = container.h3.find('span', class_ = 'lister-item-year').text
                                years.append(year)

                                imdb = float(container.strong.text)
                                imdb_ratings.append(imdb)

                                m_score = container.find('span', class_ = 'metascore').text
                                metascores.append(int(m_score))

                                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                                votes.append(int(vote))

#Examining the data:
import pandas as pd
movie_ratings = pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings,
                              'metascore': metascores,
                              'votes': votes})
print(movie_ratings.info())
movie_ratings.head(10)

movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
movie_ratings.head()

movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)

movie_ratings.describe().loc[['min', 'max'], ['imdb', 'metascore']]
movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10

movie_ratings.to_csv('movie_ratings.csv')


#Plotting the data:

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2, ax3 = fig.axes

ax1.hist(movie_ratings['imdb'], bins = 10, range = (0,10)) # bin range = 1
ax1.set_title('IMDB rating')

ax2.hist(movie_ratings['metascore'], bins = 10, range = (0,100)) # bin range = 10
ax2.set_title('Metascore')

ax3.hist(movie_ratings['n_imdb'], bins = 10, range = (0,100), histtype = 'step')
ax3.hist(movie_ratings['metascore'], bins = 10, range = (0,100), histtype = 'step')
ax3.legend(loc = 'upper left')
ax3.set_title('The Two Normalized Distributions')

for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.show()
