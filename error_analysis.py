# coding: utf-8
import numpy as np
import argparse
import json
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score

def main(predictions):

    data = []
    with open(predictions, 'r') as pred_file:
        for line in pred_file:
            data.append(json.loads(line))

    labels = [item['is_paraphrase'] for item in data]
    predictions = [item['lr_prediction'] > 0.5 for item in data]

    accuracy = accuracy_score(labels, predictions)
    p = precision_score(labels, predictions)
    r = recall_score(labels, predictions)
    f = f1_score(labels, predictions)
    print(f"Scores: accuracy {accuracy:0.03}\tprecision {p:0.03}\trecall {r:0.03}\tf1 {f:0.03}")


    # get the false negatives
    # false negatives are wrongly predicted to be negative (label is positive)
    false_negatives = [item for item in data if item['is_paraphrase']==True and item['lr_prediction']<=0.5]
    num_false_negatives = len(false_negatives)
    print(f"found {num_false_negatives} false negatives")

    # sort the false negatives
    # confident false negatives means the system prediction is very low
    false_negatives.sort(key=lambda x:x['lr_prediction'])

    print("most confident false negatives:")
    for item in false_negatives[:5]:
        #print(item)
        text_pair = item['texts']
        this_prob = item['lr_prediction']
        print(f"{this_prob:0.03}\t{text_pair[0]}\t{text_pair[1]}")


    # repeat with false positives
    # false positives are wrongly predicted to be positive (label is negative)

    false_positives = [item for item in data if item['is_paraphrase']==False and item['lr_prediction']>0.5]
    num_false_positives = len(false_positives)
    print(f"\n\nfound {num_false_positives} false positives")
    false_positives.sort(key=lambda x:x['lr_prediction'], reverse=True)

    print("most confident false positives:")
    for item in false_positives[:5]:
        #print(item)
        text_pair = item['texts']
        this_prob = item['lr_prediction']
        print(f"{this_prob:0.03}\t{text_pair[0]}\t{text_pair[1]}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prediction_json", type=str, default="benchmark_paraphrase_dev.jsonl",
                        help="json lines file containing texts, paraphrase labels and model predictions")
    args = parser.parse_args()

    main(args.prediction_json)