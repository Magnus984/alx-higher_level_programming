#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if ord(c) == i:
            return True
        else:
            continue
        return False


def uppercase(str):
    for character in str:
        if islower(character):
            print("{:c}".format(ord(character) - 32), end='')
        else:
            print("{}".format(character), end='')
    print()
