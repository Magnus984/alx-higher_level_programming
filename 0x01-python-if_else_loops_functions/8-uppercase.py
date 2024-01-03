#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if ord(c) == i:
            return True
        else:
            continue
        return False


def uppercase(str):
    mod_str = ''
    for character in str:
        if islower(character):
            mod_str += chr(ord(character) - 32)
        else:
            mod_str += character
    print(mod_str)
