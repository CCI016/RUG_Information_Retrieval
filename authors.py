from scholarly import scholarly
from serpapi import GoogleSearch
import PySimpleGUI as sg
import pprint

author_name = 'Arnold Meijster'
#Query to retrieve information from Google Scholar for the input author
search_query = scholarly.search_author(author_name)
author = scholarly.fill(next(search_query))                                      # DEBUG : scholarly.pprint(author)

#Saving the author's (Google Scholar) ID in corresponding variable
author_id = author['scholar_id']

# Parameters for performing the search through SerpAPI
serp_params = {
  "engine": "google_scholar_author",
  "hl": "en",
  "author_id": author_id,
  "num": "10",  #Number of return results after the search (SerpAPI max = 100)
  "start": "0",  #Result offset (0 = first page of results, 20 = second page, 40 = third and so on)
  "api_key": "8007fc0df66260445ed4fda679c1ae63511e60bb0b13e6baa9b4b5a46acffe0b"  # Here input your OWN SerpAPI key
}

# Searching with the above parameters for the results through SerpAPI and saving results in a dictionary
search = GoogleSearch(serp_params)
authors_dict = search.get_dict()

# Converting the values of the output's dictionary into a list to make further operations with it
x = list(authors_dict.values())
final_data = []

# Loop to traverse the list and extract all the articles with their respective title, authors, year and citation and save them into a separate list of tuples.
for i in range(0, len(x[0])) :
  data_tuple = (x[0][i]['title'], x[0][i]['authors'], x[0][i]['year'], x[0][i]['cited_by']['value'])
  final_data.append(data_tuple)

# User will select whether he would like to sort the information by year or by citations number. In case of year - index = 2, in case of citations - index = 3.
pprint.pprint(sorted(final_data, key=lambda year: year[3]))
