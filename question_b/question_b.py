#!/usr/bin/env python3
#import pdb
import re


greek = ('alpha', 'beta', 'release candidate', None)

def compare(first, second):
    """ Checks whether first is greater than second

        Numbers are compared as integers.
        Texts are compared lexicographically unless they are "alpha", "beta" or "release candidate"
    """
    if first == second:
        return 0
    #version part may have both numbers and letters
    letter_number = re.compile(r'(\d+)')
    splitted = [i for i in letter_number.split(first) if i], [i for i in letter_number.split(second) if i]
    lens = len(splitted[0]), len(splitted[1])
    for i in range(max(lens)):
        a = splitted[0][i] if i < lens[0] else None
        b = splitted[1][i] if i < lens[1] else None
        if a == b:
            continue
        ga, gb = to_greek(a), to_greek(b)
        if ga or gb:
            if ga == gb:
                continue
            return -1 if greek.index(to_greek(first)) < greek.index(to_greek(second)) else 1
        try:
            return -1 if int(first) < int(second) else 1
        except (ValueError):
            return -1 if first < second else 1
    return 0

def to_greek(version_section):
    """ Converts a section of the version number into alpha, beta, release candidate or None
    """
    if not version_section:
        return None
    splitter = re.compile(r'(\d+)')
    g = version_section.lower()
    if g ==  "rc":
        g = "release candidate"
    try:
        greek.index(g)
        return g
    except ValueError:
        return None


def remove_prefix(version_string):
    return re.sub(r'^(version|v)(\d)', r'\2', version_string)

def version_sorter(v1, v2):
    """ Return -1 if v1 is earlier than v2, 1 if it is older and 0 if it is the same. """
    # Split each part in number character boundaries
    v1, v2 = remove_prefix(v1), remove_prefix(v2)
    splitter = re.compile(r'[^\w\d\s]')
    v = splitter.split(v1.strip()), splitter.split(v2.strip())
    lens = len(v[0]), len(v[1])
    # return at the first difference, no need to seek further
    for i in range(min(lens)):
        comparison = compare(v[0][i], v[1][i])
        if comparison != 0:
            return comparison
    # If tied, the longest is the most recent 
    if lens[0] == lens[1]:
        return 0
    # if the next part of the bigger is Greek it is lower, not greater
    bigger = lens.index(max(lens))
    reverse = True if to_greek(v[bigger][min(lens)]) else False
    result = -1 if bigger else 1
    return result*-1 if reverse else result


def compare_a2b_human_friendly(str1, str2):
    answers = {
            -1: " is less than ",
            0: " is equal to ",
            1: " is greater than ",
            }
    return str1+answers[version_sorter(str1, str2)]+str2


if __name__ == '__main__':
    print("Press Ctrl+C to exit. Provide two lines on the x axis to check if they collide.")
    # Provide a command line interface
    prompt = "\n>>> "
    line1 = input("Provide line 1\n"+prompt)
    line2 = input("Provide line 2\n"+prompt)

    # Match input with or without parentheses 
    # Provide output
    print(compare_a2b_human_friendly(line1, line2))

