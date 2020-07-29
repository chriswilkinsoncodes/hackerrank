#!/usr/bin/env python3

from collections import namedtuple

n = int(input())
Grade = namedtuple('Grade', input().split())
print(f'{sum(int(Grade(*input().split()).MARKS) for _ in range(n))/n:.2f}')

''' sample data - cut/paste
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5
'''

'''first version submitted
n = int(input())
Grade = namedtuple('Grade', input().split())
total_grades = 0
for _ in range(n):
    entry = Grade(*input().split())
    total_grades += int(entry.MARKS)
print(f'{total_grades/n:.2f}')
'''

'''online solution https://www.thepoorcoder.com/hackerrank-namedtuple-solution/
from collections import namedtuple
n, Score = int(input()) , namedtuple('Score',input().split())
scores = [Score(*input().split()).MARKS for i in range(n)]
print("%.2f"% (sum(map(int,scores))/n))
'''
