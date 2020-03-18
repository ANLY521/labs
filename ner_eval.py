# coding: utf-8

from nltk.chunk import tree2conlltags
from nltk import pos_tag, ne_chunk
import argparse

# borrowed from wnuteval.py
# splits data that is separated with an extra newline
def read_ner_sents(ner_file):
    """
    Args:
        lines (Iterable[str]): the lines

    Yields:
        List[str]: sentences as list
    """

    # open data and read sentences out
    with open(ner_file, 'r') as od:
        orig_lines = od.readlines()

    sents = []
    sent = []
    stripped_lines = (line.strip() for line in orig_lines)
    for line in stripped_lines:
        if line == '':
            sents.append(sent)
            sent = []
        else:
            sent.append(line)
    sents.append(sent)
    return sents

def get_iob_ner(tokens):
    """
    :param tokens: list of string
    :return: ner tags, list of strings
    """
    # TODO: use ne_chunk to predict ner tags for each token
    ner_tags = []
    return ner_tags

def main(wnut_data, output_file):

    all_sents = read_ner_sents(wnut_data)

    with open(output_file, 'w') as pred_file:
        for sent in all_sents:
            sent_words = [line.split()[0] for line in sent]
            gold_tags = [line.split()[1] for line in sent]

            as_conll = get_iob_ner(sent_words)
            # TODO: write the token, gold standard tag, and predicted tag as tab-sep values

            # add an empty line after each sentence
            pred_file.write("\n")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--wnut_file", type=str,
                        default="emerging_entities_17/emerging.dev.conll",
                        help="wnut tsv file including annotations")
    parser.add_argument("--output_file", type=str, default="predictions.tsv",
                        help="file to write results")

    args = parser.parse_args()

    main(args.wnut_file, args.output_file)
