"""
F+T Python Course: levenshtein module

Credit where credit's due - for help with the algorithms, thanks to Wikipedia editors!
https://en.wikipedia.org/wiki/Levenshtein_distance
"""

import numpy as np
import python_course_levenshtein_py

# Simple but slow method (recursive)
def calculate_levenshtein(a, b):
    """
    Recursive implementation of Levenshtein distance.
    Returns the minimum number of edits (insert, delete, substitute)
    required to transform string a into string b.
    """
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    # If last characters are the same, skip them
    if a[-1] == b[-1]:
        cost = 0
    else:
        cost = 1

    return min(
        calculate_levenshtein(a[:-1], b) + 1,       # Deletion
        calculate_levenshtein(a, b[:-1]) + 1,       # Insertion
        calculate_levenshtein(a[:-1], b[:-1]) + cost  # Substitution
    )
# Iterative approach
def calculate_levenshtein_matrix(a, b):
    k = len(a) + 1
    l = len(b) + 1
    matrix = np.zeros((k, l), dtype=int)

    # Initialize first row and column
    for i in range(k):
        matrix[i][0] = i
    for j in range(l):
        matrix[0][j] = j

    # Fill the matrix
    for i in range(1, k):
        for j in range(1, l):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # deletion
                matrix[i][j - 1] + 1,      # insertion
                matrix[i - 1][j - 1] + cost  # substitution
            )

    # Final result = edit distance
    result = matrix[-1, -1]
    return result
