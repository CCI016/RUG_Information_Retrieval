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

In the Graphical User Interface we have an input field, a menu with one or two choices and a button.
The user should input the name of the Author he is interested in searching, then if available input an interval in the papers user is interested in viewing, for example [1,5] meaning user wants to view papers with index 1 and 5, or [1-5] meaning user wants to view papers with index 1,2,3,4 and 5. Afterwards user will press on the button to select his choice. After processing, the results will appear in the same window on user's screen. 

General workflow of the application :

Our application is divided into three different files, each corresponds to the action the user wants to perform. The first action, described in the first part of the assignment is retrieving the histograms of the publication year's and publishers of the articles for the input author. In order to do this, the user must run the file **publications.py**. The second file **citing.py** is for the actions described in the second part of assignment, what it does it is creating three histograms for all the papers citing the selected papers of the author, the histograms contains the journal or the conference name where the article appears, the publication years of the articles, and the publisher of the articles citing the indicated article of the author that was input by the user. Finally, the third file **selfcit.py** calculate the self citations for the indicated article of the input author by the user, meaning that if the author of the article cited his article himself, it will be counted as a self citation.

Below some screenshots will be attached :




PART 1 ( Histograms of publication year's and publishers of the author's articles)

![assignment2_part1_full](https://user-images.githubusercontent.com/61204251/135566581-2ad9aa26-316c-4616-ab2a-ccfb308b81f9.PNG)


PART 2 ( Histograms for the citing papers of the indicated paper of the author)
Indicated only the index numbers of the author's articles :

![assignment2_part2_numbers](https://user-images.githubusercontent.com/61204251/135566656-bd6b1001-6461-4257-aeb2-07c45092b57c.PNG)

Indicating an interval of indexes of the author's articles :
![assignment2_part2_interval](https://user-images.githubusercontent.com/61204251/135566687-0a855cc0-a3ce-4139-bf5e-6614a730fd2e.PNG)

PART 3 (Self-citations of the author's articles) :

![assignment2_part3](https://user-images.githubusercontent.com/61204251/135566718-c673cf35-1e91-4f4b-9fb5-83cafc005730.PNG)

And now by interval :

![assignment2_part3_interval](https://user-images.githubusercontent.com/61204251/135566732-053f2ab7-c8e4-40f8-a250-ae454c2b5c04.PNG)


