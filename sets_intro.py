#!/usr/bin/env python3

def average(array):
    return sum(set(array))/len(set(array))



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

'''
sample input
10
161 182 161 154 176 170 167 171 170 174
output
169.375
'''
