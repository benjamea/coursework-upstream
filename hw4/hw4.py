"""
CMSC 14100
Winter 2026
Homework 4

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

LETTER = 0
DIGIT = 1
SPECIAL = 2

# Exercise 1
def count_number_of_each(password):
    """
    Count letters, digits, and special characters in a password.

    Args:
        password (str): The password to analyze

    Returns:
        list: [letter_count, digit_count, special_count]
    """
    counts = [0, 0, 0]
    for char in password:
        char_code = ord(char)
        if 97 <= char_code <= 122:  # a-z
            counts[LETTER] += 1
        elif 48 <= char_code <= 57:  # 0-9
            counts[DIGIT] += 1
        elif 33 <= char_code <= 38:  # ! " # $ % &
            counts[SPECIAL] += 1

    return counts

# Exercise 2
def compare(input, password, wildcards):
    """
    Compare user input to actual password with wildcard support.

    Args:
        input (str): The password the user typed
        password (str): The actual stored password
        wildcards (list): List of wildcard characters

    Returns:
        int: -1 if match, otherwise index of first mismatch
    """
    min_len = len(input)
    if len(password) < min_len:
        min_len = len(password)

    for i in range(min_len):
        if password[i] in wildcards:
            continue
        if input[i] != password[i]:
            return i

    if len(input) == len(password):
        return -1
    else:

        return min_len


# Exercise 3
def compute_strength(password):
    """
    Compute the strength of a password.

    Args:
        password (str): The password to evaluate

    Returns:
        int: The strength score (non-negative integer)
    """
    strength = 0

    for char in password:
        char_code = ord(char)
        if 48 <= char_code <= 57:  # digits 0-9
            strength += 2
        elif 65 <= char_code <= 90:  # uppercase A-Z
            strength += 1
        elif 33 <= char_code <= 47:  # special ! through /
            strength += 2

    if len(password) > 8:
        strength += 3

    return strength


# Exercise 4
def brute_force_attack(length, password):
    """
    Simulate a brute-force attack to guess a password.

    Args:
        length (int): The length of the password
        password (str): The password to guess

    Returns:
        int: Number of attempts to guess the password
    """
    assert length == len(password), \
       "The value of length parameter must the length of the password."
    guess = ['a'] * length
    attempts = 0

    while True:
        attempts += 1
        if ''.join(guess) == password:
            return attempts

        # Increment from the right
        pos = length - 1
        while pos >= 0:
            if guess[pos] == 'z':
                guess[pos] = 'a'
                pos -= 1
            else:
                guess[pos] = chr(ord(guess[pos]) + 1)
                break


# Exercise 5
def create_password(phrase, strength):
    """
    Create a password from a phrase using first letters of each word.

    Args:
        phrase (str): The phrase to create password from
        strength (int): The desired minimum strength

    Returns:
        str: The generated password
    """
    words = phrase.split()
    password = ""

    for word in words:
        password = password + word[0]

    while compute_strength(password) < strength:
        password = password + "!"

    return password


