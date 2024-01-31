#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
    """prints a text with two new lines after each '.', '?', and ':'.

    Args:
        text(str): text to be parsed.
    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punct = ['.', '?', ':']
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1
    while i < len(text):
        print("{}".format(text[i]), end='')
        if text[i] == "\n" or text[i] in punct:
            if text[i] in punct:
                print()
                print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
