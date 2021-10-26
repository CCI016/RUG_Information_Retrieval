from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse
  
# We decided to split the links into two categories :
# Links with the same domain and different domains : i.e cs.rug.nl is the domain we start crawling on, but rug.nl would be considered as another domain
# This will make it more clear displaying the graph, we would see when the crawler is entering external links from the starting web page.
same_domain_urls = []
diff_domain_urls = []
starting_url = "http://www.cs.rug.nl/infosys" # The url we will begin to crawl on
depth = 2 # Value of the depth the algorithm must crawl on.


# Function to crawl the web page with the input url
def crawler_func(starting_url):
    temp = []
    starting_domain = urlparse(starting_url).netloc
  
    response = requests.get(starting_url).text
    soup = BeautifulSoup(response, "lxml")
  
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

            if starting_domain not in link and link not in diff_domain_urls:
                #print("Extern - {}".format(link))
                diff_domain_urls.append(link)

            if starting_domain in link and link not in same_domain_urls:
                #print("Intern - {}".format(link))
                same_domain_urls.append(link)
                temp.append(link)

    return temp
  
  

queue = []
queue.append(starting_url)
for j in range(depth):
    for count in range(len(queue)):
        url = queue.pop(0)
        urls = crawler_func(url)
        for i in urls:
            queue.append(i)

print(same_domain_urls)
print("\n")
print("\n")
print("\n")
print(diff_domain_urls)
				