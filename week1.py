#!/usr/bin/env python
import argparse
from collections import Counter, defaultdict
from nltk import word_tokenize

def words_used_n_times(word_count_dict, n):
    """
    Finds keys in a Counter of vocabulary items where the word is used n times
    :param word_count_dict: dictionary where keys are str and values are counts
    :param n: int
    :return: list of strings
    """
    n_times = []
    # TODO 6: define this function
    return n_times

def count_lines(text_file):

    book_lines = []
    with open(text_file, 'r') as open_file:
        for line in open_file:
            book_lines.append(line)

    print(f"{len(book_lines)} lines")
    print()

    # leading and trailing whitespace isn't important for text
    book_lines = [line.strip() for line in book_lines]

    # some lines are blank - keep only lines with something on them
    # the truth value of the empty string is False
    book_lines = [line for line in book_lines if line]

    # below this line: lab

    # 1. Import nltk and use word_tokenize on every line

    tokenized_lines = []

    print("Tokenized lines:")
    print(tokenized_lines[:5])

    print()

    # Normalization is important when surface representations don't match, but the meaning is the same.
    # "Case folding" is the most common type
    # 2. Create a dictionary that maps each lowercase type to the original cases found

    # can also do this with sets, but students are likely more familiar with list
    case_dict = defaultdict(list)

    example_words = ['whale', 'is', "double"]
    for word in example_words:
        if word not in case_dict:
            print(f"Word {word} not found")
        print(f"cases found for type {word}: {case_dict[word]}")

    print()

    # We often measure word frequency - i.e. the count of how often each type occurs
    # hint: try a Counter object
    # 3. Make a dictionary of case-folded word frequency (count tokens of each lowercase type in the file)

    # sum can flatten the list of token lists, or this can be done with an iterator
    lower_token_count = {}
    for word in example_words:
        print(f"tokens of type {word}: {lower_token_count.get(word)}")

    # However, sometimes we can't do anything with words that occur too few times
    # 4. Count how many words occur less than 10 times and print a few examples

    total_vocab_size = len(lower_token_count)
    min_count = 5

    infrequent_words = []
    num_infrequent = len(infrequent_words)
    #print(f"{num_infrequent} types of {total_vocab_size} total are infrequent, {num_infrequent / total_vocab_size:0.03f}")
    print(f"some infrequent words: {infrequent_words[:10]}")

    print()

    # 5. Fill in the stub function at the top

    word_counts = [1, 10, 100]

    for n in word_counts:
        these_words = words_used_n_times(lower_token_count, n)
        print(f"{len(these_words)} used {n} times")
        print(these_words[:10])

    # 6. Run your code on another .txt file
    # change run configurations, set different --path. Do not change the python code



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the lines in a text file')
    parser.add_argument('--path', type=str,
                        help='path to the file to count')

    args = parser.parse_args()
    count_lines(args.path)
