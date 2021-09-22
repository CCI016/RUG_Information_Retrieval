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
The user should input the name of the Author he is interested in, then choose one of the two variants for sorting the results, and afterwards press on the button : "Search for Author". After processing, the results will appear in the same window on user's screen. User has option to generate another page of results by clicking the button : "Next Page".

Input:
![Step1](https://user-images.githubusercontent.com/61204251/134287995-28bc255c-192a-4785-ace6-aa038e03ec80.png)

Selecting the filter by which means we will sort the result : 
![Step2](https://user-images.githubusercontent.com/61204251/134288021-4b0484a9-ef6d-477a-9b42-afa38f4d3dbb.png)

Result if sorted by Year of publication:
![YearSorted](https://user-images.githubusercontent.com/61204251/134288255-4331178b-4cf5-4b7a-b134-41ce71308aee.png)


or by number of citations :
![CitSorted](https://user-images.githubusercontent.com/61204251/134288034-9f4ecd31-90a6-4fac-bb38-069df1e1041e.png)

The first page of results :
![EinsteinPage1](https://user-images.githubusercontent.com/61204251/134288045-e6af8c76-2791-4b6a-86e7-4144b42a8046.png)

After clicking the button "Next page" :
![EinsteinPage2](https://user-images.githubusercontent.com/61204251/134288052-90109902-9df9-46d3-82ca-8a58be1175b1.png)

General workflow of the application :

We receive a string with the name of Author input by the user, this string is then used as a query parameter to the scholarly package. As the output from scholarly we opt to extract the unique author ID on Google Scholar platform. This ID is then used as a parameter in performing the search through SerpAPI. The output following this search is then parsed and inserted in a special list of tuples, where each tuple consists of Article's title, author's, year of publication and number of citations. Depending on the user choice, this list is sorted by the given parameter. As the last step, the list is used to draw the final final table which is displayed to the user as the output of the application.
