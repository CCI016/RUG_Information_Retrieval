from scholarly import scholarly
from serpapi import GoogleSearch
from tkinter import *
from tkinter import ttk
import pprint

# INITIALIZING GUI
root = Tk()
root.geometry('1240x768')
root.title('Google Scholar Author Articles Search')
root.configure(bg='#D6ADB4')
style = ttk.Style()

# Function triggered by the option menu from the guy, to select the user choice and save it for further use
def option_changed(option) :
  global param
  if choice_var.get() == 'Year' :
    param = 3
  else :
    param = 4

# Function that is called when the button to search authors is pressed
def search_button_command():

  global auth_search
  author_name = auth_search.get()

  #Query to retrieve information from Google Scholar for the input author
  search_query = scholarly.search_author(author_name)
  author = scholarly.fill(next(search_query))

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
  for i in range(0, int(serp_params['num'])) :
    data_tuple = (i+1, x[3][i]['title'], x[3][i]['authors'], x[3][i]['year'], x[3][i]['cited_by']['value'])
    final_data.append(data_tuple)

  # User will select whether he would like to sort the information by year or by citations index. In case of year - index = 3, in case of citations - index = 4.
  final_data = sorted(final_data, key=lambda year: year[param])

  # Section that displays on screen the total number of citations and calls the function to make the table with publications
  citations_num_total = StringVar()
  citations_num_total.set("Total number of citations of this author : " + str(x[4]['table'][0]['citations']['all']))
  Label(root,textvariable=citations_num_total).place(x=50,y=600)
  create_table(final_data, len(final_data))


# GUI SECTION contains all the elements from the GUI
author_label = Label(root,text="Search Author", bg="#B2CBEA").place(x=500,y=25)
auth_search = Entry(root, width = 28)
auth_search.focus_set()
auth_search.place(x=600,y=25)

choice_var = StringVar()
choice_var.set("  Articles by:   ")
option_sort = ('Year', 'Citations')

Label(root,text="Sort in terms of", bg="#B2CBEA").place(x=500,y=65)
chosen_sort = OptionMenu(root, choice_var,*option_sort, command= option_changed)
chosen_sort.place(x=600,y=55)

search_button = Button(root, text = "Search for Author", command = search_button_command, bg="#FFDF32")
search_button.place(x=550,y=95)

# Function that creates the table with the 
def create_table(data, table_height):
  table = ttk.Treeview(root, column=("No", "Publication Title", "Authors", "Year", "Citations"), show='headings', height= table_height)
  table.column("# 1", anchor=CENTER,width=20)
  table.heading("# 1", text="No")
  table.column("# 2", anchor=W,width=500)
  table.heading("# 2", text="Publication Title")
  table.column("# 3", anchor=W,width=460)
  table.heading("# 3", text="Authors")
  table.column("# 4", anchor=CENTER,width=50)
  table.heading("# 4", text="Year")
  table.column("# 5", anchor=CENTER,width=55)
  table.heading("# 5", text="Citations")

  var1 = len(data)
  for i in range(0, var1):
    x = list(data[i])
    x[0] = i + 1
    data[i] = tuple(x)
    table.insert('','end',text='1', values=data[i])

  table.place(x=100,y=160)


root.mainloop()
