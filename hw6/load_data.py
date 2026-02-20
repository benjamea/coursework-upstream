"""
CMSC 14100
Winter 2026

Data Loading Functions for Homework #6
"""

import sys
import json


def load_docs(filename):
    """
    Load json data from a file.

    Args:
        filename (str): name of the json file

    Returns (List[Dict]): A list of dictionaries, where each row
        in the json file is stored in a dictionary.
    """
    assert filename.endswith(".json")

    try:
        with open(filename) as f:
            data = json.load(f)
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)
    
    return data
    

def top_ngrams(ngrams_with_scores, k):
    """
    Return the top-k n-grams ranked by score.
    
    Args:
        ngrams_with_scores (dict[tuple[str, ...], float]): mapping n-grams to scores
        k (int): number of n-grams to return
    
    Returns (list[tuple[str, float]]): A list of the top-k n-grams and their 
        scores, sorted by descending score
    """
    assert k > 0, "k must be a positive integer"

    # Sort n-grams by descending TF-IDF score
    ranked = sorted(ngrams_with_scores.items(), key=lambda x: x[1], reverse=True)

    # Print top k n-gram tuples
    for i, (ng, score) in enumerate(ranked[:k], 1):
        ng = " ".join(ng)
        print(f"{i}. {ng:20}: {score:.4f}")
