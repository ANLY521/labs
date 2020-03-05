# coding: utf-8
import numpy as np
import argparse
import pickle
from sklearn.metrics import f1_score, precision_score, recall_score

def main(predictions):

    with open(predictions, 'rb') as pred_file:
        data = pickle.load(pred_file)

    print(data.keys())
    labels = data['labels']
    predictions = data['predictions'][:,1]
    texts = data['texts']

    predictions_ = predictions>=0.5
    accuracy = (predictions_==labels).mean()
    p = precision_score(labels, predictions_)
    r = recall_score(labels, predictions_)
    f = f1_score(labels, predictions_)
    print(f"Scores: accuracy {accuracy:0.03}\tprecision {p:0.03}\trecall {r:0.03}\tf1 {f:0.03}")


    # get the false negatives
    # false negatives are wrongly predicted to be negative (label is positive)
    # you can get check for these conditions using loops, but numpy.where is a nice way
    false_negative = np.where(np.logical_and(labels==1, predictions_==0))
    # get the indexes
    false_negative_probabilities = predictions[false_negative]
    num_false_negatives = false_negative_probabilities.shape[0]
    print(f"found {num_false_negatives} false negatives")
    false_negative_texts = [texts[i] for i in false_negative[0]]

    # sort the false negatives
    # confident false negatives means the system prediction is very low
    false_negative_argsort = np.argsort(false_negative_probabilities)
    print(false_negative_probabilities[false_negative_argsort])

    print("most confident false negatives:")
    for i in false_negative_argsort[:5]:
        this_prob = false_negative_probabilities[i]
        text_pair = false_negative_texts[i]
        print(f"{this_prob:0.03}\t{text_pair[0]}\t{text_pair[1]}")


    # repeat with false positives
    # false positives are wrongly predicted to be positive (label is negative)
    false_positive = np.where(np.logical_and(labels==0, predictions_==1))
    # get the indexes
    false_positive_probabilities = predictions[false_positive]
    num_false_positives = false_positive_probabilities.shape[0]
    print(f"found {num_false_positives} false positives")
    false_positive_texts = [texts[i] for i in false_positive[0]]

    # confident false positives means the system prediction is very high
    false_positive_argsort = np.argsort(false_positive_probabilities)[::-1]
    print(false_positive_probabilities[false_positive_argsort])

    print("most confident false negatives:")
    for i in false_positive_argsort[:5]:
        this_prob = false_positive_probabilities[i]
        text_pair = false_positive_texts[i]
        print(f"{this_prob:0.03}\t{text_pair[0]}\t{text_pair[1]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prediction_pkl", type=str, default="lr_predictions.pkl",
                        help="pickle containing texts, paraphrase labels and model predictions")
    args = parser.parse_args()

    main(args.prediction_pkl)