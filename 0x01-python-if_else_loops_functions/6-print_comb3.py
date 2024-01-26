#!/usr/bin/python3
for i in range(0, 10):
    for e in range(i + 1, 10):
        if i == 8 and e == 9:
            print('89')
        else:
            print('{}{}'.format(i, e), end=", ")
