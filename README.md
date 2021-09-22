# RUG_Information_Retrieval

Our application runs on **Python**.

## Packages used

For this Project we will use Scholarly Package for Python
https://github.com/scholarly-python-package/scholarly

Installation :
By using pip3 to install from pypi
```bash
$ pip3 install scholarly
```

Also we will use GoogleSearch Package from SerpAPI https://serpapi.com/
To install:
```bash
$ pip install google-search-results
```

And finally for the GUI of our application we will use tkinter package https://docs.python.org/3/library/tkinter.html#a-very-quick-look-at-tcl-tk
Installation:
```bash
$ pip install tk
```

## How does the application work?

From the users perspective : 

In the Graphical User Interface we have an input field, a menu with two choices and a button.
The user should input the name of the Author he is interested in, then choose one of the two variants for sorting the results, and afterwards press on the button : "Search for Author". After processing the results appear in the same window on user's screen.

Input:

![Step2](https://user-images.githubusercontent.com/61204251/134193130-80bc18b0-928c-4796-949e-c059253c5c4e.png)

Result if sorted by Year of publication:

![YearSorted](https://user-images.githubusercontent.com/61204251/134193305-155c98cd-2318-4b28-910c-ccafcf217cda.png)

or by number of citations :

![CitSorted](https://user-images.githubusercontent.com/61204251/134193343-d92e404e-d496-4fa3-99ea-4f9bc56e46ee.png)

General workflow of the application :

We receive a string with the name of Author input by the user, this string is then used as a query parameter to the scholarly package. As the output from scholarly we opt to extract the unique author ID on Google Scholar platform. This ID is then used as a parameter in performing the search through SerpAPI. The output following this search is then parsed and inserted in a special list of tuples, where each tuple consists of Article's title, author's, year of publication and number of citations. Depending on the user choice, this list is sorted by the given parameter. As the last step, the list is used to draw the final final table which is displayed to the user as the output of the application.
