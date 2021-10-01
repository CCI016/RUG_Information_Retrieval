from scholarly import scholarly
from serpapi import GoogleSearch
from tkinter import *
from tkinter import ttk
from collections import Counter
import re


# INITIALIZING GUI
root = Tk()
root.geometry('1240x768')
root.title('Google Scholar Authors Publication Search')
root.configure(bg='#D6ADB4')
style = ttk.Style()

# Function that will be executed once the main button is pressed
def search_button_command():
    global auth_search
    global papers_search
    author_name = auth_search.get()
    selected_papers = papers_search.get()
    titles = []
    years = []
    citations = []
    authors = []
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
        "num": "20",  #Number of return results after the search (SerpAPI max = 100)
        "start": 0,  #Result offset (0 = first page of results, 20 = second page, 40 = third and so on)
        "api_key": "7bded33ae74eb4f9f7922a14a3e6b68ba00718d28f7176285a908146260b4582"  # Here input your OWN SerpAPI key
    }

    search = GoogleSearch(serp_params)
    author_dict = search.get_dict()

    # Saving the Google Scholar name for further comparisons, for example from George Azzopardi we will get G Azzopardi, the name as the author is mentioned in the articles.
    scholar_author_name = author_dict['articles'][0]['authors'].split(",")[0]

    # For the selected papers, extract the title, year, citation number, authors and the cites_id parameter, that will be used for further search
    for i in selected_papers:
        titles.append(author_dict['articles'][i]['title'])
        years.append(author_dict['articles'][i]['year'])
        citations.append(author_dict['articles'][i]['cited_by']['value'])
        authors.append(author_dict['articles'][i]['authors'])
        data.append(author_dict['articles'][i]['cited_by']['cites_id'])

    search_citationsID(scholar_author_name, titles, authors, years, citations, data)

# Function used to search the articles citing the original input article by the 'cites_id' parameter
def search_citationsID(scholar_author_name, titles, authors, years, citations, data):
    final_res = []
    counter = 0
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
            "api_key": "7bded33ae74eb4f9f7922a14a3e6b68ba00718d28f7176285a908146260b4582"
        }
        search = GoogleSearch(params)
        results = search.get_dict()

        # Loop to count the self-citations ammount for each article, basically if the author of the main article is the same with the author that cites it, it means we have a self-citation
        for j in range (0, len(results['organic_results'])):
            try:
                for x in range (0, len(results['organic_results'][j]['publication_info']['authors'])):
                    results['organic_results'][j]['publication_info']['authors'][x]['name'] == scholar_author_name
                    counter = counter + 1
            except KeyError:
                counter = counter
        # Finally append all the accumulated data for the indicated article and add it to the final result.
        data_tuple = (titles[i], authors[i], years[i], citations[i], counter, citations[i] - counter)
        final_res.append(data_tuple)
        counter = 0

    create_table(final_res)

# Function that creates the table with the table of the self citations of an article
def create_table(data):
    table = ttk.Treeview(root, column=("No", "Title", "Authors", "Publication Year", "Citations", "Self-citations","Non-self-citations"), show='headings', height= 15)
    table.column("# 1", anchor=CENTER,width=25)
    table.heading("# 1", text="No")
    table.column("# 2", anchor=W,width=300)
    table.heading("# 2", text="Title")
    table.column("# 3", anchor=W,width=300)
    table.heading("# 3", text="Authors")
    table.column("# 4", anchor=CENTER,width=150)
    table.heading("# 4", text="Publication Year")
    table.column("# 5", anchor=CENTER,width=100)
    table.heading("# 5", text="Citations")
    table.column("# 6", anchor=CENTER,width=100)
    table.heading("# 6", text="Self-citations")
    table.column("# 7", anchor=CENTER,width=120)
    table.heading("# 7", text="Non-self-citations")

    vsb = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    vsb.place(x=205+965+10, y=202, height=300+20)

    table.configure(yscrollcommand=vsb.set)

    for i in range(0, len(data)):
        data[i] = (i+1,) + data[i]
        table.insert('','end',text='1', values=data[i])

    table.place(x=100,y=200)


# GUI SECTION - contains all the elements from the GUI
author_label = Label(root,text="Search Author", bg="#B2CBEA").place(x=500,y=15)
auth_search = Entry(root, width = 28)
auth_search.focus_set()
auth_search.place(x=600,y=15)

papers_label = Label(root,text="Selected Papers", bg="#B2CBEA").place(x=500,y=45)
papers_search = Entry(root,width=20)
papers_search.place(x=600,y=45)


search_button = Button(root, text = "Calculate Self Citations", command = search_button_command, bg="#FFDF32")
search_button.place(x=550,y=75)

histogram_label = Label(root, text= "List of author's articles",font=("Helvetica", 24),fg="#ffffff",bg="#000000").place(x=500, y = 110)

root.mainloop()