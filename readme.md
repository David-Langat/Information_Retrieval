
# Information Retrieval System

## Overview

This project is an Information Retrieval (IR) system that processes a collection of news articles from the RCV1v2 dataset. It parses the documents, applies various text processing techniques, and ranks them according to user queries using two different retrieval models: **TF-IDF** and **BM25**.

## Features

- **Document Parsing**: Parses XML documents to extract relevant text content.
- **Text Preprocessing**: Includes stop-word removal, stemming (using the Porter2 algorithm), and normalization.
- **TF-IDF Model**: Implements the Term Frequency-Inverse Document Frequency model for ranking documents.
- **BM25 Model**: Implements the Okapi BM25 ranking function, a state-of-the-art probabilistic model.
- **Query Processing**: Parses user queries and ranks documents based on relevance.

## Algorithms Used

### 1. Term Frequency-Inverse Document Frequency (TF-IDF)

TF-IDF is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.

#### a. Term Frequency (TF)

The term frequency is the number of times a term appears in a document. In this project, we use a logarithmic scale for the term frequency to dampen the effect of high-frequency terms.

```
tf(t, d) = log(f(t, d)) + 1
```

where `f(t, d)` is the raw frequency of term `t` in document `d`.

#### b. Inverse Document Frequency (IDF)

The inverse document frequency is a measure of how much information the word provides, i.e., whether the term is common or rare across all documents.

```
idf(t, D) = log(N / (df(t) + 1))
```

where `N` is the total number of documents in the corpus and `df(t)` is the number of documents containing the term `t`.

#### c. TF-IDF Score

The TF-IDF score is the product of the TF and IDF scores.

```
tfidf(t, d, D) = tf(t, d) * idf(t, D)
```

### 2. Okapi BM25

BM25 is a ranking function based on the probabilistic retrieval framework. It ranks a set of documents based on the query terms appearing in each document, regardless of the inter-relationship between the query terms at query time.

The BM25 score for a document `D` and a query `Q` containing terms `q1, q2, ..., qn` is calculated as follows:

```
score(D, Q) = Σ [ IDF(qi) * (f(qi, D) * (k1 + 1)) / (f(qi, D) + k1 * (1 - b + b * |D| / avgdl)) ]
```

where:
- `f(qi, D)` is the frequency of term `qi` in document `D`.
- `|D|` is the length of the document `D`.
- `avgdl` is the average document length in the text collection.
- `k1` and `b` are free parameters, usually chosen as `k1 = 1.2` and `b = 0.75`.
- `IDF(qi)` is the IDF of the query term `qi`.

## Project Structure

```
├── RCV1v2/                  # Contains the XML documents and common English words list
├── stemming/                # Contains stemming algorithms
│   ├── porter2.py           # Porter2 stemming algorithm used in the project
│   └── ...
├── .gitignore
├── bm25_ir_model.py         # Implementation of the BM25 model
├── main.py                  # Main entry point of the program
├── parse_documents_queries.py # Handles parsing of documents and queries
├── Rcv1Doc.py               # Class representing a document
├── readme.md                # This file
├── tfidf_ir_model.py        # Implementation of the TF-IDF model
├── *.txt                    # Output files
└── ...
```

## Setup and Usage

### Prerequisites

- Python 3.x
- PyCharm (or any other Python IDE)

### Running the Script

1.  **Clone the repository.**
2.  **Open the project in PyCharm.**
3.  **Configure the script arguments:**
    - Right-click on `main.py`.
    - Select `Modify Run Configuration`.
    - In the `Script parameters` field, enter `\RCV1v2`.
    - Click `Apply` and then `OK`.
4.  **Run the `main.py` script.**

Alternatively, you can run the script from the terminal:

```bash
py .\main.py \RCV1v2
```

## Output

The script will generate the following output files:

-   `parse_documents_queries_result.txt`: Contains the parsed terms for each document and a sample query.
-   `tfidf_ir_model_results.txt`: Contains the top 20 TF-IDF weighted terms for each document and the ranking of documents for a set of queries.
-   `bm25_ir_model_results.txt`: Contains the BM25 scores for each document for a set of test queries.
