#!/usr/bin/env python3

import re


def collide(line1, line2):
    """ Return true if the two lines overlap and false otherwise."""
    line1 = min(line1), max(line1)
    line2 = min(line2), max(line2)
    if line2[0] <= line1[0] <= line2[1]:
        return True
    if line2[0] <= line1[1] <= line2[1]:
        return True
    if line1[0] <= line2[0] <= line1[1]:
        return True
    if line1[0] <= line2[1] <= line1[1]:
        return True
    return False


def cli_match(user_input):
    """ convert user input in a tuple of integers"""
    pattern = re.compile(r'\s*\(?([+-]?\d+)[,\s]\s*([+-]?\d+)\)?\s*')
    m = pattern.match(user_input)
    return (int(m.group(1)),int(m.group(2)))


if __name__ == '__main__':

    print("Press Ctrl+C to exit. Provide two lines on the x axis to check if they collide.")
    # Provide a command line interface
    prompt = "\n>>> "
    line1 = input("Provide line 1\n"+prompt)
    line2 = input("Provide line 2\n"+prompt)

    # Match input with or without parentheses 
    # Provide output
    print(collide(cli_match(line1), cli_match(line2)))

