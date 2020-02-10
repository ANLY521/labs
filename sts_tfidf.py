# coding: utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy.stats import pearsonr
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import argparse


def preprocess_text(text):
    """Preprocess one sentence: tokenizes, lowercases, applies the Porter stemmer,
     removes punctuation tokens and stopwords.
     Returns a string of tokens joined by whitespace."""
    return " ".join(text)


def load_sts(sts_data):
    # read the dataset
    texts = []
    labels = []

    return texts, labels


def main(sts_data):

    texts, labels = load_sts(sts_data)

    # get a single list of texts to determine vocabulary and document frequency
    # create a TfidfVectorizer
    # fit to the training data


    # Now fit another vectorizer to preprocessed texts
    # Can normalization like removing stopwords remove differences that aren't meaningful?
    # Use token_pattern "\S+" to split on spaces
    preproc_train_texts = [preprocess_text(text) for text in texts]



    # compute cosine similarity for each pair of sentences, both with and without preprocessing
    cos_sims = []
    cos_sims_preproc = []

    for pair in texts:
        t1,t2 = pair

    # measure the correlations
    pearson = 0.0
    preproc_pearson = 0.0
    print(f"default settings: r={pearson:.03}")
    print(f"preprocessed text: r={preproc_pearson:.03}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sts_data", type=str, default="../strings_for_similarity/stsbenchmark/sts-dev.csv",
                        help="tab separated sts data in benchmark format")
    args = parser.parse_args()

    main(args.sts_data)