#!/usr/bin/python3

# Create a function def pascal_triangle(n):
# that returns a list of lists of integers
# representing the Pascal’s triangle of n:


def pascal_triangle(n):
    """Returns Empty list If n <= 0"""
    if n <= 0:
        return []

    triangle = []
    line = []
    start_line = []
    for s in range(0, n + 1):
        line = [t > 0 and t < s - 1 and s > 2 and start_line[t-1] +
                start_line[t] or 1 for t in range(0, s)]
        start_line = line
        triangle += [line]
    return triangle[1:]
