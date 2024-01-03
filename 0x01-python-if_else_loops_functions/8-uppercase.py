#!/usr/bin/python3
def uppercase(str):
    mod_str = ''
    for character in str:
        if ord(character) in range(ord('a'), ord('z') + 1):
            mod_str += chr(ord(character) - 32)
        else:
            mod_str += character
    print(mod_str)
