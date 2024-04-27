import string
import sys
import glob,os
from stemming.porter2 import stem
from Rcv1Doc import Rcv1Doc



def get_stopwords():
        inputpath = (os.getcwd() + sys.argv[1])
        os.chdir(inputpath)
        stopwords_f = open('common-english-words.txt', 'r')
        stop_words = stopwords_f.read().split(',')
        stopwords_f.close()
        os.chdir('..')
        return stop_words

def parse_documents_queries():  
    #handling our output(python closes automatically at the end of the block hence the reason I decide to use 'with')
    with open('parse_documents_queries_result.txt', 'w') as outfile:
        inputpath = (os.getcwd() + sys.argv[1])  #Assuming the data in a folder in the same directory as this file
        #parse the documents
        document_collection = parse_rcv1v2(get_stopwords(), inputpath)
        for (key,value) in document_collection.items():
            print(f'\n\nDocument {key} contains {len(value.terms)} terms and have {value.doc_len} words', file=outfile)
           #get the terms dictionary and sort it in descending order
            value.terms = {k: v for k, v in sorted(value.terms.items(), key=lambda item: item[1], reverse=True)}
            for (term, freq)in value.terms.items():
                print(f'{term} : {freq}', file=outfile)
        #query the documents
        query0 = 'CANADA: Sherritt to buy Dynatec, spin off unit, canada.'
        query_results = parse_query(query0,get_stopwords())
        print(f'\n\nQuery: {query0}\n\nThe parsed query:\n\n{query_results}', file =outfile)
    outfile.close()


def parse_rcv1v2(stop_words, inputpath):
    #local variables
    document_collection = {}                      #A dictonary collection of document objects as values and their ids as keys.
    os.chdir(inputpath)                             #change working directory to the inputpath variable
    for file in glob.glob('*.xml'):                 #Iterate through all files with .xml
        document = Rcv1Doc(docId= 0,doc_len = 0, terms = {})    #Initializing a document object for the current file
        start_end = False                           #Variable to signal the end of the document id section
        for line in open(file):                     #iterate through each line within the list
            line=line.strip()                       #remove the \n tags in the list
            if(start_end == False):
                if line.startswith("<newsitem "):
                    for part in line.split():
                        if part.startswith("itemid="):
                            document.docId = part.split("=")[1].split("\"")[1]      #get the document id and store it as an attribute for the document object
                            break 
                if line.startswith("<text>"):
                    start_end = True
            elif line.startswith("</text>"):
                break
            else:
                line = line.replace("<p>", "").replace("</p>", "")
                line = line.translate(str.maketrans('','', string.digits)).translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
                line = line.replace("\\s+", " ")
                for term in line.split():                      #I split the line into words. A word is a sequence of characters terminated by a whitespace or punctuation.
                    document.doc_len = document.doc_len + 1
                    term = stem(term.lower()) 
                    if len(term) > 2 and term not in stop_words:  
                        document.add_term(term)                     # I add terms into the document object. A term is a stem of a word that has more than 2 characters and is not a common english word.
                        
        document_collection[document.docId] = document        
    os.chdir('..')
    return document_collection


def parse_query(query0 ,stop_words):
    #local variables
    parsed_query = {}                           #dictionary that has the stems(terms) as its keys 
    
    query0 = query0.translate(str.maketrans('','', string.digits)).translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    query0 = query0.replace("\\s+", " ")
    for term in query0.split(): 
        term = stem(term.lower()) 
        if len(term) > 2 and term not in stop_words:
            try:
                parsed_query[term] += 1
            except KeyError:  
                parsed_query[term] = 1
    return parsed_query
    

