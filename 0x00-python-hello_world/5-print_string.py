#!/usr/bin/python3
str = "Holberton School"
for i in range(3):
    if i == 2:
        print(str)
        continue
    print(str, end='')

print(str[:9])
