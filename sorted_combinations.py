#!/usr/bin/env python3

from itertools import combinations_with_replacement as cwr


if __name__ == '__main__':
    word, n = input().split()
    # word = sorted(word)
    print('\n'.join([''.join(i) for i in cwr(sorted(word), int(n))]))