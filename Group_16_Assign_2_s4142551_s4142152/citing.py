from scholarly import scholarly
from serpapi import GoogleSearch
from tkinter import *
from tkinter import ttk
from collections import Counter
import re


# INITIALIZING GUI
root = Tk()
root.geometry('1240x980')
root.title('Google Scholar Authors Publication Search')
root.configure(bg='#D6ADB4')
style = ttk.Style()

def search_button_command():
    global auth_search
    global papers_search
    author_name = auth_search.get()
    selected_papers = papers_search.get()
    data = []

    #Removing the square brackets from the input
    selected_papers = re.sub("\[|\]","",selected_papers)
    #Parsing the selected papers input, if it is a interval make a list from x to y ([x,y]).
    if "-" in selected_papers:
        selected_papers = selected_papers.split("-")
        temp = [int(x) for x in selected_papers]
        selected_papers = list(range(temp[0],temp[1]+1))
    else:
        #In case we have just numbers followed by a "," make a list of these numbers
        selected_papers = selected_papers.split(",")
        selected_papers = [int(x) for x in selected_papers]

    #Query to retrieve information from Google Scholar for the input author
    search_query = scholarly.search_author(author_name)
    author = scholarly.fill(next(search_query), sections=['publications'])

    #Saving the author's (Google Scholar) ID in corresponding variable
    author_id = author['scholar_id']

    serp_params = {
        "engine": "google_scholar_author",
        "hl": "en",
        "author_id": author_id,
        "num": "100",  #Number of return results after the search (SerpAPI max = 100)
        "start": 0,  #Result offset (0 = first page of results, 20 = second page, 40 = third and so on)
        "api_key": "8310b39bad35cb6e13f501d4f76e43970d51850fa4d78657d74d8fc027787c24"  # Here input your OWN SerpAPI key
    }

    search = GoogleSearch(serp_params)
    author_dict = search.get_dict()
    
    #Loop to extract all the 'cites_id' for the input articles
    for i in selected_papers:
        data.append(author_dict['articles'][i]['cited_by']['cites_id'])

    search_citationsID(data)

# Function used to search the articles citing the original input article by the 'cites_id' parameter
def search_citationsID(data):
    final_res = []
    links = []
    summary = []

    # By assignment requirements we have to process only 20 of the cites_id
    if len(data) > 20:
        citations_number = 20
    else :
        citations_number = len(data)

    for i in range(0, citations_number):
        cites_id = data[i]
        params = {
            "engine": "google_scholar",
            "cites": cites_id,
            "api_key": "8310b39bad35cb6e13f501d4f76e43970d51850fa4d78657d74d8fc027787c24"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        for i in range (0, len(results['organic_results'])):
            links.append(results['organic_results'][i]['link'])
            summary.append(results['organic_results'][i]['publication_info']['summary'])

    summary_parser(summary)

# Function to parse the summary tag from the previous JSON, which contains the journal or conference name where the article is presented, article's publication year, and publisher
def summary_parser(data):
    data_size = len(data)

    journal = []
    publisher = []
    year = []

    for i in range (0, len(data)):
        if len(data[i].split(" - ")) == 3 :
            journal.append(data[i].split(" - ")[1])
            publisher.append(data[i].split(" - ")[2])
        else:
            publisher.append(data[i].split(" - ")[1])
            journal.append("N\A")
        if journal[i] != "N\A" and journal[i].isnumeric() == False:
            year.append(journal[i].split(", ")[1])
            journal[i] = journal[i].split(", ")[0]
            journal[i] = re.sub("\…","",journal[i])
        else :
            year.append(journal[i])

    year = Counter(year)
    year = sorted(year.items())
    year.pop()
    year.pop()
    year.pop()

    publisher = Counter(publisher)
    publisher = sorted(publisher.items())

    journal = Counter(journal)
    journal = sorted(journal.items())
    
    create_hysto1(journal)
    create_hysto2(year)
    create_hysto3(publisher)

# Function to draw the histogram table for the journal or conference's where article was presented
def create_hysto1(data):
    hist = ttk.Treeview(root, column=("No", "Source (journal or conference) names", "Quantity"), show='headings', height= 10)
    hist.column("# 1", anchor=CENTER,width=25)
    hist.heading("# 1", text="No")
    hist.column("# 2", anchor=CENTER,width=500)
    hist.heading("# 2", text="Source (journal or conference) names")
    hist.column("# 3", anchor=CENTER,width=460)
    hist.heading("# 3", text="Quantity")

    vsb = ttk.Scrollbar(root, orient="vertical", command=hist.yview)
    vsb.place(x=100+965+5, y=202, height=200+20)

    hist.configure(yscrollcommand=vsb.set)

    for i in range(0, len(data)):
        data[i] = (i+1,) + data[i]
        hist.insert('','end',text='1', values=data[i])

    hist.place(x=100,y=200)

# Function to draw the histogram of the publication years of the article
def create_hysto2(data):
    hist = ttk.Treeview(root, column=("No", "Publication Year", "Quantity"), show='headings', height= 10)
    hist.column("# 1", anchor=CENTER,width=25)
    hist.heading("# 1", text="No")
    hist.column("# 2", anchor=CENTER,width=500)
    hist.heading("# 2", text="Publication Year")
    hist.column("# 3", anchor=CENTER,width=460)
    hist.heading("# 3", text="Quantity")

    vsb = ttk.Scrollbar(root, orient="vertical", command=hist.yview)
    vsb.place(x=100+965+5, y=452, height=200+20)

    hist.configure(yscrollcommand=vsb.set)

    for i in range(0, len(data)):
        data[i] = (i+1,) + data[i]
        hist.insert('','end',text='1', values=data[i])

    hist.place(x=100,y=450)

# Function to draw the histogram of the publishers of the article
def create_hysto3(data):
    hist = ttk.Treeview(root, column=("No", "Publisher", "Quantity"), show='headings', height= 10)
    hist.column("# 1", anchor=CENTER,width=25)
    hist.heading("# 1", text="No")
    hist.column("# 2", anchor=CENTER,width=500)
    hist.heading("# 2", text="Publisher")
    hist.column("# 3", anchor=CENTER,width=460)
    hist.heading("# 3", text="Quantity")

    vsb = ttk.Scrollbar(root, orient="vertical", command=hist.yview)
    vsb.place(x=100+965+5, y=702, height=200+20)

    hist.configure(yscrollcommand=vsb.set)

    for i in range(0, len(data)):
        data[i] = (i+1,) + data[i]
        hist.insert('','end',text='1', values=data[i])

    hist.place(x=100,y=700)


# GUI SECTION - contains all the elements from the GUI
author_label = Label(root,text="Search Author", bg="#B2CBEA").place(x=500,y=15)
auth_search = Entry(root, width = 28)
auth_search.focus_set()
auth_search.place(x=600,y=15)

papers_label = Label(root,text="Selected Papers", bg="#B2CBEA").place(x=500,y=45)
papers_search = Entry(root,width=20)
papers_search.place(x=600,y=45)


search_button = Button(root, text = "Submit", command = search_button_command, bg="#FFDF32")
search_button.place(x=550,y=75)

histogram_label = Label(root, text= "Histograms of all cited papers of the selected author's paper",font=("Helvetica", 24),fg="#ffffff",bg="#000000").place(x=200, y = 110)

root.mainloop()