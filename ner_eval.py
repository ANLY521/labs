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
    # named entity chunking happens off POS tags
    sent_with_pos = pos_tag(tokens)
    # run the default named entity recognizer
    nes = ne_chunk(sent_with_pos)
    # convert to conll format
    as_iob = tree2conlltags(nes)
    return [ner for token,pos,ner in as_iob]

def main(wnut_data, output_file):

    all_sents = read_ner_sents(wnut_data)

    with open(output_file, 'w') as pred_file:
        for sent in all_sents:
            sent_words = [line.split()[0] for line in sent]
            gold_tags = [line.split()[1] for line in sent]

            as_conll = get_iob_ner(sent_words)

            for i, tag_prediction in enumerate(as_conll):
                original_word = sent_words[i]
                if "-" in tag_prediction:
                    iob, entity = tag_prediction.split("-")
                    if entity not in ["PERSON", "ORGANIZATION",
                                      "GPE", "FACILITY", "LOCATION"]:
                        tag_prediction = "O"
                    else:
                        if entity == "ORGANIZATION":
                            entity = "corporation"
                        if entity in ["FACILITY", "GPE"]:
                            entity = "location"
                        tag_prediction = f"{iob}-{entity.lower()}"
                line_as_str = f"{original_word}\t{gold_tags[i]}\t{tag_prediction}\n"
                pred_file.write(line_as_str)
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
