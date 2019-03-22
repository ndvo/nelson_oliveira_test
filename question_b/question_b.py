#!/usr/bin/env python3

import re


greek = (r for r in 'alpha', 'beta', 'release candidate', None)

def compare(first, second):
    if first == second:
        return 0
    if greek(first) or greek(second):
        return -1 if greek.index(first) < greek.index(second) else 1
    try:
        return -1 if int(first) < int(second) else 1
    except ValueError e:
        return -1 if first < second else 1

def greek(version_section):
    """Converts a section of the version number into alpha, beta, release candidate or None"""
    g = version_section.lower()
    try:
        greek.index(g)
        return g
    except ValueError e:
        return None


def version_sorter(v1, v2):
    """ Return -1 if v1 is earlier than v2, 1 if it is older and 0 if it is the same. """
    # Splits the string on non alphanumeric characters
    non_word = re.compile(r'[^\w\d]')
    numberleter = re.compile(r'(\d+)')
    v1 = non_word.split(v1)
    v2 = non_word.split(v2)
    lens = (len(v1), len(v2))
    for i in range(min(lens)):
        numberletter1 = numberleter.split(v1[i])
        numberletter2 = numberleter.split(v2[i])
        nllens = (len(numberletter1), len(numberletter2))
        for ii in range(min(nllens)):

        first = numberleter.split(v1[i])
        second = numberleter.split(v2[i])
    # If tied 
    return 0 if lens[0] == lens[1] else -1 if !release_candidate.match(v2[-1]) else 1


    # Split each part in number character boundaries

    # Lexicografical order from left to rigth, provided that rc comes before 

class VersionPart():
    pattern = re.compile(r'^\s*(\d+)-?((release|rc|release-candidate|beta|alpha)(\d))?([a-z]*)')

    def __init__(self, content):

        print(content)
        m = self.pattern.match(content)
        self.number = m.get(1)
        self.type = m.get(3)
        self.type_number = m.get(4)
        self.letter = m.get(5)

    def __cmp__(self, other):
        return -1

a = VersionPart(1)
b = VersionPart(2)

a < b




def split_in_parts(version_string):
    separator = find_separator(version_string)
    (name, version) = strip_name(version_string)
    print("version string splitted", version_string.split(separator))
    return [VersionPart(part) for part in version_string.split(separator)]

def find_separator(version_string):
    return '.'

def strip_name(version_string):
    return version_string.split(' ')

def compare_a2b_human_friendly(str1, str2):
    


if __name__ == '__main__':

    print("Press Ctrl+C to exit. Provide two lines on the x axis to check if they collide.")
    # Provide a command line interface
    prompt = "\n>>> "
    line1 = input("Provide line 1\n"+prompt)
    line2 = input("Provide line 2\n"+prompt)

    # Match input with or without parentheses 
    # Provide output
    print(collide(cli_match(line1), cli_match(line2)))

