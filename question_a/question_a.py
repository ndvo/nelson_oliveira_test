#!/usr/bin/env python3

import re



def collide(line1, line2):
    return True



def cli_match(user_input):
    pattern = re.compile(r'\s*\(?([+-]?\d+)[,\s]\s*([+-]?\d+)\)?[,\s]\s*\s*\(?([+-]?\d+)[,\s]\s*([+-]?\d+)\)?\s*')
    print(pattern)
    m = pattern.match(user_input)
    return (m.group(1),m.group(2)), (m.group(3),m.group(4))


if __name__ == '__main__':

    print("Press Ctrl+C to exit. Provide two lines on the x axis to check if they collide.")
    # Provide a command line interface
    prompt = "\n>>> "
    line1 = input("Provide line 1\n"+prompt)
    line2 = input("Provide line 2\n"+prompt)

    # Match input with or without parentheses 
    # Provide output
    print(collide(cli_match(line1), cli_match(line2)))

