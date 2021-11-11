from urllib.request import urljoin
from urllib.request import urlparse
import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plot
  
# We decided to split the links into two categories :
# Links with the same domain and different domains : i.e cs.rug.nl is the domain we start crawling on, but rug.nl would be considered as another domain
# This will make it more clear displaying the graph, we would see when the crawler is entering external links from the starting web page.
G = nx.Graph()
same_domain_urls = []
diff_domain_urls = []
starting_url = "http://www.cs.rug.nl/infosys" # The url we will begin to crawl on
G.add_node(starting_url)
depth = 2 # Value of the depth the algorithm must crawl on.


# Function to crawl the web page with the input url
def crawler_func(starting_url):
    html_docs = []
    urls = []
    starting_domain = urlparse(starting_url).netloc
  
    response = requests.get(starting_url).text
    soup = BeautifulSoup(response, "lxml")
    html_docs.append(soup)
    G.add_node(soup)
  
    for anchor in soup.findAll("a"):
        link = anchor.attrs.get("href")

	#URLs follow a specific format <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
	# Below we are parsing the link we extracted from the anchor after href attribute
        if (link != ""):
            link = urljoin(starting_url, link)
            parsed_link = urlparse(link)
            link = parsed_link.scheme
            link += "://"
            link += parsed_link.netloc
            link += parsed_link.path
            G.add_edge(soup, html_docs[len(html_docs) - 2])

            if starting_domain not in link and link not in diff_domain_urls:
                diff_domain_urls.append(link)

            if starting_domain in link and link not in same_domain_urls:
                same_domain_urls.append(link)
                urls.append(link)

    return urls
  
  
# Traverse using BFS untill the goal depth is traversed.
bfs_queue = []
bfs_queue.append(starting_url)
for j in range(depth):
    for x in range(len(bfs_queue)):
        url = bfs_queue.pop(0)
        urls = crawler_func(url)
        for i in urls:
            bfs_queue.append(i)
print("Links with the same domain : ")
print(same_domain_urls)
print("\n")
print("Links with different domain : ")
print(diff_domain_urls)
nx.draw(G)
plot.show()