"""
CMSC 14100
Winter 2026
Homework 6

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from load_data import load_docs, top_ngrams

import math

REPLACEMENTS = {
    '!': ' ',
    '"': "'",
    '#': ' ',
    '$': ' ',
    '%': ' ',
    '&': ' ',
    "'": "'",
    '(': ' ',
    ')': ' ',
    '*': ' ',
    '+': ' ',
    ',': ' ',
    '-': ' ',
    '.': ' ',
    '/': ' ',
    ':': ' ',
    ';': ' ',
    '<': ' ',
    '=': ' ',
    '>': ' ',
    '?': ' ',
    '@': ' ',
    '[': ' ',
    '\\': ' ',
    ']': ' ',
    '^': ' ',
    '_': ' ',
    '`': ' ',
    '{': ' ',
    '|': ' ',
    '}': ' ',
    '~': ' '
 }


# Exercise 1
def normalize_text(text):
    """
    Normalize a piece of text by converting to lowercase, applying
    character replacements, and collapsing whitespace.

    Input:
        text (str): the original text

    Returns (str): the normalized text
    """
    text = text.lower()
    for char, replacement in REPLACEMENTS.items():
        text = text.replace(char, replacement)
    return " ".join(text.split())


# Exercise 2
def process_doc(doc):
    """
    Process a document by normalizing its title and content,
    and tokenizing the result into a single list of tokens.

    Input:
        doc (dict): a document dictionary with 'title' and 'content' keys

    Returns (dict): a new dictionary with 'title', 'content', and 'tokens' keys
    """
    norm_title = normalize_text(doc["title"])
    norm_content = normalize_text(doc["content"])
    tokens = norm_title.split() + norm_content.split()
    return {"title": norm_title, "content": norm_content, "tokens": tokens}


# Exercise 3
def get_ngram_counts(processed_doc, n):
    """
    Compute n-gram counts for a processed document, caching the result.

    Inputs:
        processed_doc (dict): a processed document dictionary
        n (int): the n-gram size

    Returns (dict): a dictionary mapping n-grams (tuples) to their counts
    """
    assert n > 0, "n must be a positive integer"
    key = f"ngram_counts_{n}"
    if key in processed_doc:
        return processed_doc[key]
    tokens = processed_doc["tokens"]
    counts = {}
    for i in range(len(tokens) - n + 1):
        ngram = tuple(tokens[i:i + n])
        counts[ngram] = counts.get(ngram, 0) + 1
    processed_doc[key] = counts
    return counts


# Exercise 4
def distinct_n(processed_doc, n):
    """
    Compute the distinct-n value for a processed document.

    Inputs:
        processed_doc (dict): a processed document dictionary
        n (int): the n-gram size

    Returns (float): the distinct-n score
    """
    assert n > 0, "n must be a positive integer"
    counts = get_ngram_counts(processed_doc, n)
    total = sum(counts.values())
    if total == 0:
        return 0.0
    return len(counts) / total


# Exercise 5
def get_corpus_stats(processed_docs, n):
    """
    Compute corpus-level n-gram statistics from a list of processed documents.

    Inputs:
        processed_docs (list): a list of processed document dictionaries
        n (int): the n-gram size

    Returns (dict): a dictionary with 'counts' and 'doc_freq' keys
    """
    assert n > 0, "n must be a positive integer"
    counts = {}
    doc_freq = {}
    for doc in processed_docs:
        ngram_counts = get_ngram_counts(doc, n)
        for ngram, count in ngram_counts.items():
            counts[ngram] = counts.get(ngram, 0) + count
            doc_freq[ngram] = doc_freq.get(ngram, 0) + 1
    return {"counts": counts, "doc_freq": doc_freq}


# Exercise 6
def compute_tf(processed_doc, n):
    """
    Compute term frequency (TF) values for n-grams in a processed document.

    Inputs:
        processed_doc (dict): a processed document dictionary
        n (int): the n-gram size

    Returns (dict): a dictionary mapping n-grams to their TF values
    """
    assert n > 0, "n must be a positive integer"
    counts = get_ngram_counts(processed_doc, n)
    total = sum(counts.values())
    if total == 0:
        return {}
    return {ngram: count / total for ngram, count in counts.items()}


# Exercise 7
def compute_idf(processed_docs, n):
    """
    Compute inverse document frequency (IDF) values for n-grams in a corpus.

    Inputs:
        processed_docs (list): a list of processed document dictionaries
        n (int): the n-gram size

    Returns (dict): a dictionary mapping n-grams to their IDF values
    """
    stats = get_corpus_stats(processed_docs, n)
    num_docs = len(processed_docs)
    return {ngram: math.log(num_docs / freq)
            for ngram, freq in stats["doc_freq"].items()}


# Exercise 8
def compute_tfidf(processed_docs, processed_doc, n):
    """
    Compute TF-IDF scores for all n-grams in a document.

    Inputs:
        processed_docs (list): a list of processed document dictionaries
        processed_doc (dict): a processed document dictionary
        n (int): the n-gram size

    Returns (dict): a dictionary mapping n-grams to their TF-IDF scores
    """
    tf = compute_tf(processed_doc, n)
    idf = compute_idf(processed_docs, n)
    return {ngram: tf_val * idf[ngram]
            for ngram, tf_val in tf.items() if ngram in idf}
