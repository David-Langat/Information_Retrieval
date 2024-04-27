if __name__ == '__main__':

    import sys
    import os
    from parse_documents_queries import parse_documents_queries
    from tfidf_ir_model import tfidf_ir_model
    from bm25_ir_model import bm25_ir_model

    #to run the program in terminal just type the lines between the dollar sign  $ py .\main.py \\RCV1v2  $  this is assuming the documents ot be parsed are in the folder RCV1v2
    if len(sys.argv) != 2:
        sys.stderr.write("USAGE: %s <coll-file>\n" % sys.argv[0])
        sys.exit()


    parse_documents_queries()
    tfidf_ir_model()
    bm25_ir_model()            