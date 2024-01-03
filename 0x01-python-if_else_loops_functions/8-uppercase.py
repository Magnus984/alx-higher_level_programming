#!/usr/bin/python
def uppercase(str):
    for character in str:
        if ord(character) in range(ord('a'), ord('z') + 1):
            character = chr(ord(character) - 32)
        print("{}".format(character), end='')
    print()
