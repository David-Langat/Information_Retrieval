############################################# RUNNING IN PYCHARM #############################################################################################################


 Information Retrieval

This Python script is designed to perform information retrieval tasks on a collection of documents using various algorithms. Below are the instructions on how to run the script:

1. Environment Setup:
   - Ensure you have Python installed on your system. You can download Python from https://www.python.org/downloads/. This project was built using python version 3.12.3.
   - Install PyCharm, an Integrated Development Environment (IDE) for Python, which can be downloaded from https://www.jetbrains.com/pycharm/download/.

2. Project Setup in PyCharm:
   - Open PyCharm and open the folder 'langat_11462167'. The folder should have the following:
   
   Folders:

   _pycahce_
   RCV1v2   - This folders contains the xml documents to be parsed and the common_english_words.txt
   Stemming

   Files:

   parse_documents_queries_results.txt
   tfidf_ir_model_results.txt
   bm25_ir_model_results.txt
   main.py
   parse_documents_queries.py
   tfidf_ir_model.py
   bm25_ir_model.py
   RCV1v2.py
   readme.txt
  
3. Running the Script in PyCharm:
   - Once the project is set up and the script arguments are configured, you can run the script in PyCharm:
     - Right-click on the main.py file in the project explorer.
     - Select Modify Run Configuration.
     - type '\\RCV1v2' into the script parameters field and click apply.
     - Right-click main and select Run 'main'.

4. Viewing Output:
   - After running the script, the output will be generated in the following files:
     - parse_documents_queries_results.txt
     - tfidf_ir_model_results.txt
     - bm25_ir_model_results.txt
   - These files will contain the results of the information retrieval tasks performed by the script.

5. Troubleshooting:
   - If you encounter any issues while running the script, ensure that you have provided the correct path to the collection of documents and that the required Python packages are .
installed

################################################################### RUN IN TERMINAL#########################################################################################################
 #to run the program in terminal just type the lines between the dollar sign  $ py .\main.py \\RCV1v2  $  this is assuming the documents ot be parsed are in the folder RCV1v2
