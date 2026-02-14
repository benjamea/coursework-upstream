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
    raise ValueError("Not implemented")


# Exercise 2
def process_doc(doc):
    raise ValueError("Not implemented")


# Exercise 3
def get_ngram_counts(processed_doc, n):
    assert n > 0, "n must be a positive integer"
    raise ValueError("Not implemented")


# Exercise 4
def distinct_n(processed_doc, n):
    assert n > 0, "n must be a positive integer"
    raise ValueError("Not implemented")


# Exercise 5
def get_corpus_stats(processed_docs, n):
    assert n > 0, "n must be a positive integer"
    raise ValueError("Not implemented")


# Exercise 6
def compute_tf(processed_doc, n):
    assert n > 0, "n must be a positive integer"
    raise ValueError("Not implemented")


# Exercise 7
def compute_idf(processed_docs, n):
    raise ValueError("Not implemented")


# Exercise 8
def compute_tfidf(processed_docs, processed_doc, n):
    raise ValueError("Not implemented")
