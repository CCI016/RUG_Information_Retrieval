import pathlib
import requests
from bs4 import BeautifulSoup
import queue

def crawl_func(starting_anchor, url):
    anchor_search = queue.Queue()
    found_urls = []
    while True:
        if not starting_anchor:
            starting_anchor = '/'
        
        response = requests.request('GET', url + starting_anchor)
        soup = BeautifulSoup(response.text, "lxml")
        anchors = local_anchors_search(starting_anchor, soup)
        if anchors:
            for a in anchors:
                new_url = url + a
                if new_url in found_urls:
                    continue
                if not pathlib.Path(a).suffix:
                    anchor_search.put(a)
                found_urls.append(new_url)
                print(new_url)

        if anchor_search.empty():
            break
        starting_anchor = anchor_search.get()
        print(anchor_search.get())
    return found_urls

def local_anchors_search(starting_anchor, soup):
    anchors = []
    for link in soup.find_all('a'):
        anchor = link.attrs["href"] if "href" in link.attrs else ''
        print(starting_anchor)
        if anchor.startswith(starting_anchor):
            anchors.append(anchor)
    return anchors

def main():
    url = "http://www.cs.rug.nl/infosys" #http://www.cs.rug.nl/infosys
    start_anchor = "/"
    urls = crawl_func(start_anchor, url)
    print(len(urls), urls)

if __name__ == "__main__":
    main()

