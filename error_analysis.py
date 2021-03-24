# coding: utf-8
import argparse

def main(predictions):

    # print metrics to confirm correct loading
    accuracy = 0.0
    p = 0.0
    r = 0.0
    f = 0.0
    print(f"Scores: accuracy {accuracy:0.03}\tprecision {p:0.03}\trecall {r:0.03}\tf1 {f:0.03}")


    # get the false negatives
    # false negatives are wrongly predicted to be negative (label is positive)
    # you can get check for these conditions using loops
    num_false_negatives = 0
    print(f"found {num_false_negatives} false negatives")

    # sort the false negatives
    # confident false negatives means the system prediction is very low
    # print texts and system prediction
    # HINT: check out the kwarg "key" in .sort
    print("most confident false negatives:")

    # repeat with false positives
    # false positives are wrongly predicted to be positive (label is negative)
    num_false_positives = 0
    print(f"found {num_false_positives} false positives")
    print("most confident false positives:")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prediction_json", type=str, default="benchmark_paraphrase_dev.jsonl",
                        help="json lines file containing texts, paraphrase labels and model predictions")
    args = parser.parse_args()

    main(args.prediction_json)