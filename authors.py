from scholarly import scholarly
from serpapi import GoogleSearch
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
  "start": "100",  #Result offset (0 = first page of results, 20 = second page, 40 = third and so on)
  "api_key": "8007fc0df66260445ed4fda679c1ae63511e60bb0b13e6baa9b4b5a46acffe0b"  # Here input your OWN SerpAPI key
}

search = GoogleSearch(serp_params)
authors_dict = search.get_dict()

# for x in authors_dict :

pprint.pprint(authors_dict)