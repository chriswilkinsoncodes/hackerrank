#!/usr/bin/env python3

_, int_list = input(), input().split()
print(all(int(x) > 0 for x in int_list) and any(s == s[::-1] for s in int_list))
