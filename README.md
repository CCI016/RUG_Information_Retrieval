# RUG_Information_Retrieval

Our application runs on **Python**.

## Assignment 2

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




## Assignment 3
## Packages Used
For this assignment we will use GoogleSearch Package from SerpAPI https://serpapi.com/
To install:
```bash
$ pip install google-search-results
```
Also we will use matplotlib package for plotting the graph which can be installed by theh following command
```bash
$ pip install matplotlib
```

## Report
Our goal in this assignment is to quantitatively evaluate the web search results.

In order to achieve this, we will evaluate 4 search algorithms that are : Google, Bing, DuckDuckGo and Yahoo.

As the baseline for our evaluation we will take the search results obtained after using the engine Google, we have taken this decision as Google is the most popular searching engine nowadays, therefore we consider all the results from Google to be relevant for our query. Based on this relevant set, we will evaluate the remaining three search algorithms.

Eventhough we have set the number of wanted results in SerpApi params to 20 by default, for some queries we do not obtain 20 results. For example, for the default query given in the SerpApi which is "Coffee" we have the following output : Length of Bing results  15 Length of DuckDuckGo results  20 Length of Yahoo results  5
During the testing of our program we have used a lot of other queries, but most of the time the length of Bing and Yahoo results is under the estabilished argument (top_n).


In our evaluation we will use the following metrics : 
**Precision and recall** are the measures used in the information retrieval domain to measure how well an information retrieval system retrieves the relevant documents requested by a user. The measures are defined as follows:

Precision  =  Total number of documents retrieved that are relevant/Total number of documents that are retrieved.

Recall  =  Total number of documents retrieved that are relevant/Total number of relevant documents in the database.
 
Also we will plot a graph of these 2 metrics.

The **F-score Measure** is a way of combining the precision and recall of the model, and it is defined as the harmonic mean of the model’s precision and recall.

The F-score is commonly used for evaluating information retrieval systems such as search engines

However we went further with the query "Coffee" and we obtained the following results :

**BING Search Algorithm**

(6.666666666666667, 10.0)    -- (Precision, Recall) values

P@5 for Bing is  6.666666666666667

P@7 for Bing is  6.666666666666667

F Measure for Bing is  30.0


![BingCurve](https://user-images.githubusercontent.com/61204251/136451878-603d771a-88a4-4378-b8af-c7c1d5a245ce.PNG)

**DuckDuckGo Search Algorithm**

(15.0, 30.0)    -- (Precision, Recall) values

P@5 for DuckDuckGo is  10.0

P@7 for DuckDuckGo is  10.0

F Measure for DuckDuckGo is  90.0


![DuckDuckGoCurve](https://user-images.githubusercontent.com/61204251/136451892-df9c2421-7401-41d6-a9c6-ba09b2a21e7e.PNG)


**Yahoo Search Algorithm**

(40.0, 20.0)   -- (Precision, Recall) values

P@5 for Yahoo is  40.0

P@7 for Yahoo is  40.0

F Measure for Yahoo is  60.0


![YahooCurve](https://user-images.githubusercontent.com/61204251/136451903-a9fe01fd-8641-48e2-adce-a5994e03f730.PNG)


By analyzing the results we came to the conclusion that for the query "Coffee" the DuckDuckGo is the seach engine that had the most similar links after performing the search on the query with the Google engine, which we consider to be the set of all relevant links. On the second place we have Yahoo, and last place is Bing. However it is important to mention that DuckDuckGo was always stable when retrieving from SerpApi the search results, but Yahoo and Bing give sometimes less results for the query, therefore it is safe to assume that if there were more results fetched after the SerpApi Yahoo Search we would observe this engine to be closer to the results given by Google.


## Assignment 5

Tne web crawler is an application that automatically surfs the web. In order to develop such an application we have used several additional libraries.

**URLLIB** which helps to operate with the urls, allowing to divide the url into parts such as scheme, netloc, to join the urls and etc.

**BS4** BeautifulSoup allows us to be able to get tags from the HTML pages.

**REQUESTS** is a library that simply operates with HTTP requests.

**NETWORKX** library used to draw the graph.

The workflow of our web crawler can be described as following : First of all we make a GET request to the first input URL, after which we extracted the URL's HTML content. As the next step, we convert this HTML content in a BeautifulSoup object, so that later on we can extract HTML tags and their contents. We are interested in anchor tag, and especially in "href" parameter, since we are looking to retrieve all links present on the page. Getting the links, we extract their domain, and look if it is the same as the initial, to know if our crawler is still on the same domain or it went further. The idea to separate the different domains links would be good when displaying data on the graph, so the graph would't be overcrowded. Since URL is formed as a tree structure, on the first level we have the starting URL, while on the next level we have all the URLs that can be accesed from inside of the input URL and so on, we have used Breadth First Search (BFS) traversal. Our web crawler is retrieving data following depth parameter, in our condition we must crawlto the depth=2, meaning that the application must crawl all urls in the given web page and in turn it must crawl all the urls within them.

Application Usage:

Our program is very easy to use, user must make sure he/she has all the libraries installed if not this can be done by the command :
```bash
$ pip install <library_name>
```
Also user must change the value of starting_url variable to his desired URL to start with and of course run the program.

## Assignment 5

Implementing a face recognition algorith using cosine difference algorithm.

Application Usage:

Our program is very easy to use, user must choose the value for rejection threshhold, number of known people and number of training images per person then to compile the python file, which can be done by the following command : 
```bash
$ python3 face_recognition.py
```

During our testing we have tried to experiment with the values of **Rejection Threshhold** between 0.1 and 1, **Number of known people and number of training images per person** with the values 5 and 10 (maximum amount of pictures available)

When analyzing the output we found the following :

Rejection threshhold affects the accuracy, the lower the threshhold is the higher accuracy we get, this is due to the fact that we "accept" only the images with the lowest possible cosine difference, meaning that the face of the compared person is the most similar as it could be to the known person.

When we increase the number of known people, the accuracy also gets higher (considering we compare with the output having the same rejection threshhold and number of trained images per person), this is caused by the fact that the more people our algorithm knows, the more testing images are accepted.

When we decrease the number of training images per person (considering we compare with the output having the same parameters as before) we observe that the accuracy also decreases, this is due to the fact that less images are supplied, and therefore there are less comparisons of the test image with the ones from database. For example, if we don't have a lot of images with the person, or images with some changes such as : glasses, beard and so on, when we encounter such a image in the test section, the algorithm can not properly compare it to the existing one.

Below is the output for all our tests. The output prints also the parameters used to generate it.



<img width="394" alt="thresh0 2" src="https://user-images.githubusercontent.com/61204251/141375316-66a9a365-48da-4475-bd4e-54d1a540619b.png">
<img width="478" alt="thresh0 5" src="https://user-images.githubusercontent.com/61204251/141375319-597e42d1-9321-4c29-bb22-78a313b8bc85.png">
<img width="449" alt="thresh0 75" src="https://user-images.githubusercontent.com/61204251/141375322-c889f152-1f81-4477-9fef-8ca151a00095.png">

<img width="489" alt="img1" src="https://user-images.githubusercontent.com/61204251/141375350-0012da00-5fd9-4cbb-9249-37044aab9895.png">
<img width="507" alt="img3" src="https://user-images.githubusercontent.com/61204251/141375357-4cdf80f7-890f-4622-bfb0-ecedc4f33b7e.png">
<img width="517" alt="img5" src="https://user-images.githubusercontent.com/61204251/141375363-0fe4ce29-fb5a-46b9-932d-d82838135c35.png">
<img width="467" alt="img8" src="https://user-images.githubusercontent.com/61204251/141375365-628f7e78-21b1-4e30-a2d2-f7fca14d8774.png">

<img width="382" alt="people3" src="https://user-images.githubusercontent.com/61204251/141375368-e684f04b-3c6d-4bc4-aff0-fe9e522be5b9.png">
<img width="497" alt="people5" src="https://user-images.githubusercontent.com/61204251/141375370-7cba3bc6-ed54-4b8b-bc9e-c3b787ad8989.png">
<img width="477" alt="people8" src="https://user-images.githubusercontent.com/61204251/141375373-b13747b3-3d6e-4f04-a660-e50d055ed914.png">

