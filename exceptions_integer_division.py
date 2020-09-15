#!/usr/bin/env python3

T = int(input())
for _ in range(T):
    num, denom = input().split()
    try:
        print(int(num)//int(denom))
    except Exception as e:
        print("Error Code:", e)

''' input sample
3
1 0
2 $
3 1
'''