# Lab repository

On weeks with homework, the lab is usually the first part of the homework and distributed in the homework repository.
On the happy weeks with no homework, the labs will be distributed through this repository.

The labs should run without crashing as-is. However, you'll need to fill in code to make them produce the right answers.

# Files

## `requirements.txt`

Use this to download the latest version of the libraries in our course environment.

## `week1.py` : refresher on tokenizing and counting vocabulary using Moby Dick.

Download the utf-8 file from [Project Gutenberg](http://www.gutenberg.org/files/2701/2701-0.txt)

Usage:
`python week1.py --path moby_dick.txt`

## `sts_tfidf.py`

This lab computes the similarity of pairs of sentences using a normalized term-document matrix and cosine similarity.
This similarity metric is evaluated as a model of semantic similariy against a gold standard using pearson correlation.

Data is from the [STS benchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark).

Usage:
`python sts_tfidf.py --sts_data stsbenchmark/sts-dev.csv`