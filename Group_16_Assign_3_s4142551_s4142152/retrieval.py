from serpapi import GoogleSearch
import matplotlib.pyplot as plt

#T Main function of retrieving the information using 4 different search algorithms (Google, Bing, DuckDuckGo, Yahoo)
def get_search_results(algo, query, top_n = 20):

    #The api key used for SerpApi searches
    api_key = "1650f41f485f2b1f307bb4c0ad1053fd8ab27b213694b3225b21072d81243312"

    links_doc = []
    # Below there are the search parameters for the algorithms, I have set the locations to Netherlands to ensure that the search engins are giving simmilar results.
    google_params = {
        "engine": algo,
        "q": query,
        "location": "Amsterdam, North Holland, Netherlands",
        "google_domain": "google.nl",
        "gl": "nl",
        "hl": "en",
        "num": top_n,
        "api_key": api_key
    }

    bing_params = {
        "engine": algo,
        "q": query,
        "google_domain": "google.nl",
        "hl": "nl",
        "gl": "nl",
        "location": "Amsterdam, North Holland, Netherlands",
        "count": top_n,
        "api_key": api_key
    }

    duck_params = {
        "engine": algo,
        "q": query,
        "kl": "nl-nl",
        "api_key": api_key
    }

    yahoo_params = {
        "engine": algo,
        "p": query,
        "yahoo_domain": "nl",
        "vc": "nl",
        "vl": "lang_en",
        "pz": top_n,
        "api_key": api_key
    }

    if algo == 'google':
        chosen_params = google_params
    
    if algo == 'bing':
        chosen_params = bing_params
    
    if algo == 'duckduckgo':
        chosen_params = duck_params

    if algo == 'yahoo':
        chosen_params = yahoo_params

    
    search = GoogleSearch(chosen_params)
    results = search.get_dict()

    # This conditional ensures that when sometimes SerpApi is not giving the required number of results, our program doesn't run in an index error
    if len(results['organic_results']) < top_n:
        max_range = len(results['organic_results'])
    else:
        max_range = top_n

    # For-loop to extract the ranked list of links obtained from the search algorithm
    for i in range(0, max_range):
        links_doc.append(results['organic_results'][i]['link'])

    return links_doc

# This function is used to calculate Retrieval Metrics such as Precision and Recall
def precision_recall(retrieved_docs, relevant_docs):

    precision_counter = 0
    precision_total = len(retrieved_docs)
    recall_total = len(relevant_docs)

    for i in range(0, precision_total):
        if retrieved_docs[i] in relevant_docs:
            precision_counter = precision_counter + 1

    precision = precision_counter / precision_total * 100
    recall = precision_counter / recall_total * 100

    return precision, recall

# This function is used to calculate Precision and Recall and also plot all the values on graph
def precision_recall_curve(retrieved_docs, relevant_docs):
    current_relevant_docs = 0
    current_number_docs = 0

    precision_y = []
    recall_x = []
    for i in range (0, len(retrieved_docs)):
        if retrieved_docs[i] in relevant_docs:
            current_relevant_docs = current_relevant_docs + 1
            current_number_docs = current_number_docs +1
        else:
            current_number_docs = current_number_docs + 1
        precision_y.append((current_relevant_docs / current_number_docs) * 100)
        recall_x.append(current_number_docs / len(retrieved_docs) * 100)

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')

    plt.plot(recall_x, precision_y, label = "Curve")

    plt.show()

# This function is used to calculate Precision at a specific point, in assignment we will use P@5 and P@7
def find_p_at_x(retrieved_docs, relevant_docs, x):
    precision_count = 0
    for i in range (0, x-1):
        if retrieved_docs[i] in relevant_docs:
            precision_count = precision_count +1
    
    return (precision_count / len(retrieved_docs) * 100)

# This function is used to calculate F_measure to Evaluate the Retrieval, formula based on : https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#F-score_/_F-measure
def find_f_measure(retrieved_docs, relevant_doc):
    F_measure = (2 * precision_recall(retrieved_docs, relevant_doc)[0] * precision_recall(retrieved_docs, relevant_doc)[1] ) / precision_recall(retrieved_docs, relevant_doc)[0] + precision_recall(retrieved_docs, relevant_doc)[1]

    return F_measure

# Main section of the program
def main():
    # Here we define our query and the search algorithms we will be using in the assignment
    search_query = "Coffee"
    search_results = {
        'google': get_search_results('google', search_query, top_n=11),
        'bing': get_search_results('bing', search_query, top_n=20),
        'duckduckgo': get_search_results('duckduckgo', search_query, top_n=20),
        'yahoo': get_search_results('yahoo', search_query, top_n=20)
    }

    #Let's consider the links that we retrieved from google to be relevant, as the Google is the most popular search engine
    relevant_doc = search_results['google']
    print("Algorithm used as the baseline for further evaluation is Google\n")
    del search_results['google']

    bing_docs = search_results['bing']
    duck_docs = search_results['duckduckgo']
    yahoo_docs = search_results['yahoo']

    #Below our program will output one-by one the results and the Evaluation Metrics for the given search algorithhms
    print ("BING Search Algorithm")
    print(precision_recall(bing_docs, relevant_doc))
    print("P@5 for Bing is " , find_p_at_x(bing_docs, relevant_doc,5))
    print("P@7 for Bing is " , find_p_at_x(bing_docs, relevant_doc,7))
    print("F Measure for Bing is " , find_f_measure(bing_docs, relevant_doc))
    precision_recall_curve(bing_docs, relevant_doc)
    print("\n")
    print("\n")


    print ("DuckDuckGo Search Algorithm")
    print(precision_recall(duck_docs, relevant_doc))
    print("P@5 for DuckDuckGo is ", find_p_at_x(duck_docs, relevant_doc,5))
    print("P@7 for DuckDuckGo is " , find_p_at_x(duck_docs, relevant_doc,7))
    print("F Measure for DuckDuckGo is ", find_f_measure(duck_docs, relevant_doc))
    precision_recall_curve(duck_docs, relevant_doc)
    print("\n")
    print("\n")


    print ("Yahoo Search Algorithm\n")
    print(precision_recall(yahoo_docs, relevant_doc))
    print("P@5 for Yahoo is ", find_p_at_x(yahoo_docs, relevant_doc,5))
    print("P@7 for Yahoo is " , find_p_at_x(yahoo_docs, relevant_doc,6))
    print("F Measure for Yahoo is " , find_f_measure(yahoo_docs, relevant_doc))
    precision_recall_curve(yahoo_docs, relevant_doc)  
    print("\n")
    print("\n")

if __name__ == "__main__":
    main()
