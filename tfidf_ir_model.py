import glob,os,sys
from math import log, sqrt
from parse_documents_queries import parse_query,parse_rcv1v2, get_stopwords

def tfidf_ir_model():
    inputpath = (os.getcwd() + sys.argv[1])  #Assuming the data in a folder in the same directory as this file
    document_collection = parse_rcv1v2(get_stopwords(), inputpath) #parse the documents
    titles = get_titles(inputpath) #Get the text in <title></text>

   
    with open('tfidf_ir_model_results.txt', 'w') as outfile:
        #ouput the document frequency into a file 
        document_frequency,total_unique_terms,total_documents = my_df(document_collection)
        print(f'There are {total_documents} documents in this data set and contains {total_unique_terms} terms', file=outfile)
        print(f'The following are the term\'s document-frequency:', file=outfile)
        for (term, freq) in document_frequency.items():
             print(f'{term} : {freq}', file=outfile)
        rank = {}
        
        # Calculate TF-IDF for each document
        for doc in document_collection.values():
            if len(doc.terms) > 20:
                tfidf = my_tfidf(doc, document_frequency, total_documents)
                # Sort by TF-IDF value in descending order and get the top 20 terms
                top_terms = sorted(tfidf.items(), key=lambda item: item[1], reverse=True)[:20]
                print(f'\nDocument {doc.getDocId()} contains {len(doc.terms)} terms:', file=outfile)
                for term, weight in top_terms:
                    print(f'{term} : {weight}', file=outfile)
                print('\n', file=outfile)
        
        #Raking score for the documents using the titles as queries
        for title in titles:
            title = title.replace("&amp;", "&").split(" - ")[0]  #I've done this to match the expected output
            print(f'\nThe Ranking result for query: {title}\n', file=outfile)
            parsed_title = parse_query(title, get_stopwords())
            rank = {}
            for doc in document_collection.values():
                tfidf = my_tfidf(doc, document_frequency, total_documents)
                ranking_score = sum(tfidf[term] for term in parsed_title if term in tfidf)
                rank[doc.getDocId()] = ranking_score

            # Sort the dictionary by value
            rank = {k: v for k, v in sorted(rank.items(), key=lambda item: item[1], reverse=True)}

            # Print sorted dictionary to file
            for doc_id, score in rank.items():
                print(f'{doc_id} : {score}', file=outfile)
 


def my_df(coll):
    total_documents = 0             #count the number of documents
    unique_terms = set()            #initialize an empty set to count the unique terms
    document_frequency = {}         #initialize an empty dictionary to store the document frequency of each term

    #Get unique terms in all documents
    for document in coll.values():
        total_documents += 1
        unique_terms.update(document.terms.keys())      #add the terms in the document to the set of unique terms

    #Calculate document frequency for each unique term
    for term in unique_terms:
        for document in coll.values():                  #iterate through all documents
            if term in document.terms:                  #check if the term is in the document
                if term in document_frequency:          #increment the document frequency of the term
                    document_frequency[term] += 1
                else:
                    document_frequency[term] = 1

    total_unique_terms = len(unique_terms)
    #sort the dictionary by value
    document_frequency = {k: v for k, v in sorted(document_frequency.items(), key=lambda item: item[1], reverse=True)}    
    return document_frequency,total_unique_terms,total_documents



def my_tfidf(doc, df, ndocs):
    tfidf = {}   #dictionary for storing the tf-idf values of terms in the document {'term': 'tfidf_weight'}
    for (term,freq) in doc.terms.items(): #get the term and its frequency in the document
        tf = log(freq) + 1
        idf = log(ndocs/df[term])
        tfidf[term] = tf * idf
    # Calculate the square root of the sum of the squares of the TF-IDF weights
    norm = sqrt(sum(weight**2 for weight in tfidf.values()))
    # Normalize the TF-IDF weights
    tfidf = {term: weight/norm for term, weight in tfidf.items()}
    tfidf = {k: v for k, v in sorted(tfidf.items(), key=lambda item: item[1], reverse=True)} #sort the tfidf dictionary by value
    return tfidf

def get_titles(inputpath): #retrieve the text in the title section. I will use this as queries to test the ir model
    titles = []  # List to store the titles of the documents
    os.chdir(inputpath)  
    #parse the title section of documents and retrieve the title
    for file in glob.glob('*.xml'):
        for line in open(file):
            line = line.strip()
            if line.startswith('<title>'):
                title = line.split('<title>')[1].split('</title>')[0]
                title = title.split(':', 1)[1].strip() if ':' in title else title  # Remove the first word and colon
                titles.append(title)            
    os.chdir('..')
    return titles
