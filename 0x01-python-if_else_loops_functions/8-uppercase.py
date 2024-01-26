#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) >= 97 and ord(n) <= 122:
            n = chr(ord(n) - 32)
        print("{}".format(n), end="")
    print()
