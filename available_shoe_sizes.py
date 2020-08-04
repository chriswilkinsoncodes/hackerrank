#!/usr/bin/env python3

# unused variable; unnecessary input
shoes = int(input())

sizes = list(input().split())
customers = int(input())
earnings = 0

for _ in range(customers):
    size, price = input().split()
    if size in sizes:
        earnings += int(price)
        sizes.remove(size)
print(earnings)

'''
sample input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
# try version using collections.Counter()
