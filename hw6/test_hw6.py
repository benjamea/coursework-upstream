"""
CMSC 14100
Winter 2026

Test code for Homework #6
"""

import hw6
from load_data import load_docs

import os
import sys
import pickle
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw6"
    

# Exercise 1
@pytest.mark.parametrize("text, expected",
                         [('ABCD', 'abcd'),
                          ('Hello   ', 'hello'),
                          ('', ''),
                          ('"Homework #6"', "'homework 6'"),
                          ('.#@', ''),
                          ("It's  CS  141!!!", "it's cs 141"),
                         ])
def test_normalize_text(text, expected):
    """ Test code for normalize_text """
    steps = [
        f"actual = hw6.normalize_text({text})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw6.normalize_text(text)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)   
        

# Exercise 2     
@pytest.mark.parametrize("original_filename, index",
                         [('corpus_1.json', 1),
                          ('corpus_1.json', 2),
                          ('corpus_2.json', 0),
                          ('corpus_2.json', 1),
                          ('corpus_2.json', 2),
                          ])
def test_process_doc(original_filename, index):
    """ Test code for process_doc """
    steps = [
        "from load_data import load_docs",
        f"docs = load_docs('./data/{original_filename}')",
        f"actual = hw6.process_doc(docs[{index}])",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    docs = load_docs(f'./data/{original_filename}')
    try:
        actual = hw6.process_doc(docs[index])
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    expected = load_docs("./data/processed_" + original_filename)[index]

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


# Exercise 3
@pytest.mark.parametrize("processed_doc, n, expected",
                         [({'title': 'a', 'contents': '', 'tokens': ['a']}, 1, {('a',): 1}),
                          ({'title': 'a', 'contents': 'b c', 'tokens': ['a', 'b', 'c']},
                           1,
                           {('a',): 1, ('b',): 1, ('c',): 1}),
                          ({'title': 'a', 'contents': 'b c', 'tokens': ['a', 'b', 'c']},
                           2,
                           {('a', 'b'): 1, ('b', 'c'): 1}),
                          ({'title': 'a', 'contents': 'a b b', 'tokens': ['a', 'a', 'b', 'b']},
                           2,
                           {('a', 'a'): 1, ('a', 'b'): 1, ('b', 'b'): 1}),
                          ({'title': 'a', 'contents': 'b c', 'tokens': ['a', 'b', 'c']},
                           3,
                           {('a', 'b', 'c'): 1}),
                          ({'title': 'a', 'contents': 'b c', 'tokens': ['a', 'b', 'c']}, 4, {}),
                          ({'title': "", 'contents': "", 'tokens': []}, 1, {}),
                          ({'title': 'a', 'contents': 'a b b', 'tokens': ['a', 'a', 'b', 'b'],
                            'ngram_counts_2': {('a', 'a'): 1, ('a', 'b'): 1, ('b', 'b'): 1}},
                           2,
                           {('a', 'a'): 1, ('a', 'b'): 1, ('b', 'b'): 1})
                         ])
def test_get_ngram_counts(processed_doc, n, expected):
    """ Test code for get_ngram_counts """
    steps = [
        f"actual = hw6.get_ngram_counts({processed_doc}, {n})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    tag =  f"ngram_counts_{n}"
    expected = processed_doc.get(tag, expected)
    check_same_ptr = tag in processed_doc
    
    try:
        actual = hw6.get_ngram_counts(processed_doc, n)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    tag =  f"ngram_counts_{n}"
    if tag not in processed_doc:
        err_msg = (f"\"{tag}\" has not been added to the dictionary passed in\n"
                   f"  for the processed_doc argument\n")
        pytest.fail(err_msg + recreate_msg)

    if processed_doc[tag] != expected:
        err_msg = (f"The value associated with \"{tag}\" in the dictionary passed in\n"
                   f"for the processed_doc argument is not correct:\n"
                   f"  The expected value is: {expected}\n"
                   f"  The actual value is: {processed_doc[tag]}\n")
        pytest.fail(err_msg + recreate_msg)

    if check_same_ptr and not (actual is expected):
        err_msg = f"The result should refer to the same pointer as processed_doc[\"{tag}\"]\n"
        pytest.fail(err_msg + recreate_msg)



# Exercise 4
@pytest.mark.parametrize("tokens, n, expected",
                         [({'title': 'a', 'contents': '', 'tokens': ['a']}, 1, 1.0),
                          ({'title': 'a', 'contents': 'b c', 'tokens': ['a', 'b', 'c']}, 2, 1.0),
                          ({'title': 'a', 'contents': 'a a a', 'tokens': ['a', 'a', 'a', 'a']},
                           1,
                           0.25),
                          ({'title': 'a', 'contents': 'a b b', 'tokens': ['a', 'a', 'b', 'b']}, 2, 1.0),
                          ({'title': 'a', 'contents': 'b a b', 'tokens': ['a', 'b', 'a', 'b']},
                           2,
                           0.6666666666666666),
                          ({'title': "", 'contents': "", 'tokens': []}, 1, 0.0)
                         ])
def test_distinct_n(tokens, n, expected):
    """ Test code for distinct_n """
    steps = [
        f"actual = hw6.distinct_n({tokens}, {n})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw6.distinct_n(tokens, n)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_equals(actual, expected) # Floating point comparison
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)    
        

# Exercise 5
@pytest.mark.parametrize("original_filename, n",
                         [('corpus_1.json', 1),
                          ('corpus_1.json', 2),
                          ('corpus_1.json', 3),
                          ('corpus_2.json', 1),
                          ('corpus_2.json', 2)
                        ])
def test_get_corpus_stats(original_filename, n):
    """ Test code for get_corpus_stats """
    steps = [
        "from load_data import load_docs",
        f"docs = load_docs('./data/{original_filename}')",
        f"processed_docs = [hw6.process_doc(doc) for doc in docs]",
        f"actual = hw6.get_corpus_stats(processed_docs, {n})",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    docs = load_docs(f'./data/{original_filename}')
    try:
        processed_docs = [hw6.process_doc(doc) for doc in docs]
        actual = hw6.get_corpus_stats(processed_docs, n)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    with open("./data/stats_" + original_filename.replace(".json", ".pkl"), "rb") as f:
        expected = pickle.load(f)[n - 1]

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
        
        
        
# Exercise 6
@pytest.mark.parametrize("original_filename, index, n",
                         [('corpus_3.json', 0, 1),
                          ('corpus_3.json', 0, 3),
                          ('corpus_3.json', 0, 50),
                          ('corpus_3.json', 1, 1),
                          ('corpus_3.json', 2, 1),
                        ])
def test_compute_tf_only(original_filename, index, n):
    """ Test code for compute_tf """
    steps = [
        "from load_data import load_docs",
        f"doc = load_docs('./data/{original_filename}')[{index}]",
        f"processed_doc = hw6.process_doc(doc)",
        f"actual = hw6.compute_tf(processed_doc, {n})",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    doc = load_docs(f'./data/{original_filename}')[index]
    try:
        processed_doc = hw6.process_doc(doc)
        actual = hw6.compute_tf(processed_doc, n)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    with open('./data/tf_corpus.pkl', "rb") as f:
        key = f'{original_filename}-{index}-{n}'
        expected = pickle.load(f)[key]

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


# Exercise 7
@pytest.mark.parametrize("original_filename, n",
                         [('corpus_1.json', 1),
                          ('corpus_1.json', 2),
                          ('corpus_1.json', 3),
                          ('corpus_1.json', 50),
                          ('corpus_2.json', 1),
                          ('corpus_3.json', 1),
                        ])
def test_compute_idf(original_filename, n):
    """ Test code for compute_idf """
    steps = [
        "from load_data import load_docs",
        f"docs = load_docs('./data/{original_filename}')",
        f"processed_docs = [hw6.process_doc(doc) for doc in docs]",
        f"actual = hw6.compute_idf(processed_docs, {n})",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    docs = load_docs(f'./data/{original_filename}')
    try:
        processed_docs = [hw6.process_doc(doc) for doc in docs]
        actual = hw6.compute_idf(processed_docs, n)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    with open('./data/idf_corpus.pkl', "rb") as f:
        key = f'{original_filename}-{n}'
        expected = pickle.load(f)[key]

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
        
        
# Exercise 8
@pytest.mark.parametrize("docs_filename, doc_filename, index, n",
                         [('corpus_1.json', 'corpus_1.json', 0, 1),
                          ('corpus_1.json', 'corpus_1.json', 1, 2),
                          ('corpus_1.json', 'corpus_1.json', 2, 3),
                          ('corpus_1.json', 'corpus_1.json', 0, 15),
                          ('corpus_2.json', 'corpus_2.json', 0, 1),
                          ('corpus_2.json', 'corpus_1.json', 2, 1),
                          ('corpus_3.json', 'corpus_1.json', 2, 1),
                          ('corpus_3.json', 'corpus_1.json', 1, 2),
                          ('corpus_3.json', 'corpus_3.json', 3, 1),
                        ])
def test_compute_tfidf(docs_filename, doc_filename, index, n):
    """ Test code for compute_tfidf """
    steps = [
        "from load_data import load_docs",
        f"docs = load_docs('./data/{docs_filename}')",
        f"processed_docs = [hw6.process_doc(d) for d in docs]",
        f"doc = load_docs('./data/{doc_filename}')[{index}]",
        f"processed_doc = hw6.process_doc(doc)",
        f"actual = hw6.compute_tfidf(processed_docs, processed_doc, {n})",
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    docs = load_docs(f'./data/{docs_filename}')
    doc = load_docs(f'./data/{doc_filename}')[index]
    try:
        processed_docs = [hw6.process_doc(d) for d in docs]
        processed_doc = hw6.process_doc(doc)
        actual = hw6.compute_tfidf(processed_docs, processed_doc, n)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    with open('./data/tfidf_corpus.pkl', "rb") as f:
        key = f'{docs_filename}-{doc_filename}-{index}-{n}'
        expected = pickle.load(f)[key]

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
