import sys,os
from math import log2
from parse_documents_queries import parse_query, get_stopwords,parse_rcv1v2
from tfidf_ir_model import my_df

def bm25_ir_model():
    inputpath = (os.getcwd() + sys.argv[1])  #Assuming the data in a folder in the same directory as this file
    document_collection = parse_rcv1v2(get_stopwords(), inputpath) #parse the documents
    document_frequency,total_unique_terms,total_documents = my_df(document_collection)
    average_length = avg_length(document_collection)
    test_query = ['The British-Fashion Awards','Rocket attacks','Broadcast Fashion Awards','stock market'] #queries provided for tests
    
    #####Test####

    with open('bm25_ir_model_results.txt', 'w') as outfile:
        print(f'Average document length for this collection is:{average_length}', file = outfile)
        for query in test_query:
            print(f'\nThe query is:{query}', file = outfile)
            print(f'The following are the BM25 score for each document:\n', file = outfile)
            
            bm25_scores = my_bm25(document_collection,query,document_frequency)
            for key,value in bm25_scores.items():
                print(f'Document ID:{key}, Doc Length:{document_collection[key].doc_len} -- BM25 Score:{value}',file = outfile)
            
            print(f'\nFor query {query}, the top-6 possible relevant documents are:',file = outfile)
            #sort by value in descending order
            bm25_scores = {k: v for k, v in sorted(bm25_scores.items(), key=lambda item: item[1], reverse=True)}
            for key,value in bm25_scores.items():
                count= 0
                if count<7:
                    print(f'{key} {value}', file = outfile)
                    count += 1
  

def avg_length(coll):
    totalDocLength = sum(doc.doc_len for doc in coll.values()) #add up all doc lengths for documents in coll 
    return totalDocLength / len(coll) if coll else 0

def my_bm25(coll,q,df):
    parsed_query = parse_query(q,get_stopwords())
    bm25_scores = {}   #empty dictionary to store the bm25 scores
    #calculacte bm25 for each document
    for document in coll.values():
        bm25 = 0 #since we are calculatiing the bm25 score for each document we have to intiate it to zero for every document
        bm25_sum = 0
        for (qterm,qfreq) in parsed_query.items():
            for (term,freq) in document.terms.items():
                if term in parsed_query:
                    bm25 = log2(1/(df[term] + 0.5)*(len(coll)- df[term]+0.5))*((2.2)*freq)/((1.2*(0.25+(0.75 * (document.doc_len/avg_length(coll)))))+freq)*((101*qfreq)/(100+qfreq))
                    bm25 = bm25/3
                    bm25_sum += bm25
                else:
                    bm25 = 0
        bm25_scores[document.docId] = bm25_sum
    return bm25_scores
