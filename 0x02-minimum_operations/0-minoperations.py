#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def countProcess(num):
    """
        Returns an integer
        If n is impossible to achieve, return 0
    """
    count = 1
    p_list = []
    value = num
    while value != 1:
        count += 1
        if value % count == 0:
            while (value % count == 0 and value != 1):
                value /= count
                p_list.append(count)

    return p_list


def minOperations(n):
    """
        Returns an integer
        If n is impossible to achieve, return 0
    """
    if n < 2 or type(n) is not int:
        return 0
    values = countProcess(n)
    return sum(values)
