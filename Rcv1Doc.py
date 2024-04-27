class Rcv1Doc:
    def __init__(self, docId,doc_len, terms = {}):
        self.docId = docId
        self.terms = terms
        self.doc_len = doc_len

    def getDocId(self):   # a method used to retrieve document ID
        return self.docId
    
    def get_term_list(self): # a method to return a sorted list of terms
        sorted_terms = {k: v for k, v in sorted(self.terms.items(), key=lambda item: item[1], reverse=True)}  # sort by value to get the frequency of terms in descending order
        return sorted_terms
    def add_term(self, term): #takes a term and tries to increase frequency if it exists in terms dictionary and
        try:
            self.terms[term] += 1
        except KeyError:
            self.terms[term] = 1

    @property #accessor for document length
    def doc_len(self):
        return self._doc_len

    @doc_len.setter #mutator for document length
    def doc_len(self, value):
        self._doc_len = value