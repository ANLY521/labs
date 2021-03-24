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


## `error_analysis.py`

This lab finds the most confident wrong predictions in system output for paraphrase identification. 
Data with labels and predictions is read from a json lines file.
The top 5 false positives and negatives are printed.

Usage:
`python error_analysis.py --prediction_json benchmark_paraphrase_dev.jsonl`


## `benchmark_paraphrase_dev.jsonl`

A file of json lines. It contains a selection of the STS Benchmark corpus with labels
converted to paraphrase, predictions of a paraphrase logistic regression, and several similarity scores.

## wnuteval.py

Taken from the WNUT17 website. Slight modifications fix import error in Python 3 and stop crashing on 
illegal tags in test data. (This fix does NOT ensure test tags are valid.)

Use with a tab-separated submission in the form:
`<original word>  <gold standard tag>   <predicted tag>`

Example usage:

`python wnuteval.py my_predictions.tsv`

## ner_eval.py

Loads WNUT data and uses `nltk`'s `ne_chunk` to predict labels for each sentence.
HINT: requires part-of-speech tagging and conversion between tree and conll formats.

Converts entity classes using the scheme described below in Entity Mapping.

Writes a flat (text) file of NER predictions that can be scored by `wnuteval.py`.

`python ner_eval.py --wnut_file emerging_entities_17/emerging.dev.conll`

### Entity mapping

 | Nltk entity type | WNUT entity  |
 | ------------- | ------------- |
 |ORGANIZATION | -> corporation |
 |PERSON | -> person |
 |LOCATION | -> location |
 |DATE | None |
 |TIME | None |
 |MONEY | None |
 |PERCENT| None |
 |FACILITY| -> location |
 |GPE | -> location |
