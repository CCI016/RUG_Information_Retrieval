from scholarly import scholarly
from serpapi import GoogleSearch
from tkinter import *
from tkinter import ttk
from collections import Counter

# INITIALIZING GUI
root = Tk()
root.geometry('1240x768')
root.title('Google Scholar Authors Publication Search')
root.configure(bg='#D6ADB4')
style = ttk.Style()

# Function that is called when the main button is pressed
def search_button_command():
    global auth_search
    author_name = auth_search.get()

    #Query to retrieve information from Google Scholar for the input author
    search_query = scholarly.search_author(author_name)
    author = scholarly.fill(next(search_query), sections=['publications'])
    #Saving the author's (Google Scholar) ID in corresponding variable
    author_id = author['scholar_id']
    pub_years = []
    for i in range (0, len(author['publications'])) :
        try:
            pub_years.append(author['publications'][i]['bib']['pub_year'])
        except KeyError:
            pub_years.append("N\A")
    pub_years = Counter(pub_years)
    pub_years = sorted(pub_years.items())
    create_hysto1(pub_years)

    serp_params = {
        "engine": "google_scholar_author",
        "hl": "en",
        "author_id": author_id,
        "num": "100",  #Number of return results after the search (SerpAPI max = 100)
        "start": 0,  #Result offset (0 = first page of results, 20 = second page, 40 = third and so on)
        "api_key": "7bded33ae74eb4f9f7922a14a3e6b68ba00718d28f7176285a908146260b4582"  # Here input your OWN SerpAPI key
    }

    # Searching with the above parameters for the results through SerpAPI and saving results in a dictionary
    search = GoogleSearch(serp_params)
    authors_dict = search.get_dict()
    # Converting the values of the output's dictionary into a list to make further operations with it
    final_data = []

    for i in range (0,int(serp_params["num"])):
        final_data.append(authors_dict['articles'][i]['citation_id'])


    publisher_search(author_id, final_data)

# Function to search the publisher of the articles using SerpAPI, by the citation id.
def publisher_search(author_id, data):

    final_res = []

    for i in range(0, len(data)):
        citation_id = data[i]
        serp_params = {
            "engine": "google_scholar_author",
            "hl": "en",
            "author_id": author_id,
            "view_op": "view_citation",
            "citation_id": citation_id,
            "api_key": "7bded33ae74eb4f9f7922a14a3e6b68ba00718d28f7176285a908146260b4582"
        }
        search = GoogleSearch(serp_params)
        results = search.get_dict()

        try :
            final_res.append(results['citation']['publisher'])
        except KeyError :
            final_res.append("N\A")

    final_res = Counter(final_res)
    final_res = sorted(final_res.items())
    create_hysto2(final_res)

# Function to draw the publication year histogram table
def create_hysto1(data):
    hist = ttk.Treeview(root, column=("No", "Publication Year", "Quantity"), show='headings', height= 10)
    hist.column("# 1", anchor=CENTER,width=25)
    hist.heading("# 1", text="No")
    hist.column("# 2", anchor=CENTER,width=500)
    hist.heading("# 2", text="Publication Year")
    hist.column("# 3", anchor=CENTER,width=460)
    hist.heading("# 3", text="Quantity")

    vsb = ttk.Scrollbar(root, orient="vertical", command=hist.yview)
    vsb.place(x=100+965+5, y=202, height=200+20)

    hist.configure(yscrollcommand=vsb.set)

    for i in range(0, len(data)):
        data[i] = (i+1,) + data[i]
        hist.insert('','end',text='1', values=data[i])

    hist.place(x=100,y=200)

# Function used to draw the publisher histogram table
def create_hysto2(data):
    hist = ttk.Treeview(root, column=("No", "Publisher", "Quantity"), show='headings', height= 10)
    hist.column("# 1", anchor=CENTER,width=25)
    hist.heading("# 1", text="No")
    hist.column("# 2", anchor=CENTER,width=500)
    hist.heading("# 2", text="Publisher")
    hist.column("# 3", anchor=CENTER,width=460)
    hist.heading("# 3", text="Quantity")

    vsb = ttk.Scrollbar(root, orient="vertical", command=hist.yview)
    vsb.place(x=100+965+5, y=502, height=200+20)

    hist.configure(yscrollcommand=vsb.set)

    for i in range(0,len(data)):
        data[i] = (i+1,) + data[i]
        hist.insert('','end',text='1', values=data[i])
    hist.place(x=100,y=500)

# GUI SECTION - contains all the elements from the GUI such as Text Labels and Buttons
author_label = Label(root,text="Search Author", bg="#B2CBEA").place(x=500,y=15)
auth_search = Entry(root, width = 28)
auth_search.focus_set()
auth_search.place(x=600,y=15)

search_button = Button(root, text = "Search for Author", command = search_button_command, bg="#FFDF32")
search_button.place(x=550,y=55)

histogram_label = Label(root, text= "Histograms of all author's papers",font=("Helvetica", 24),fg="#ffffff",bg="#000000").place(x=400, y = 90)

root.mainloop()