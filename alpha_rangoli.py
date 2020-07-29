#!/usr/bin/env python3

from string import ascii_lowercase as ll


def print_rangoli(size):
    if size == 1:
        print('a')
        return
    # l = {x:y for x, y in zip(range(1, 27), lc)}
    lc = ' ' + ll
    chars = lc[size] + '-'
    print(chars.center(4*size-3, '-'))
    for i in range(size-1, 0, -1):
        print(f'{chars}{lc[i]}{chars[::-1]}'.center(4*size-3, '-'))
        chars += lc[i] + '-'
    chars = chars[:-2]
    for i in range(2, size+1):
        chars = chars[:-2]
        print(f'{chars}{lc[i]}{chars[::-1]}'.center(4*size-3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
