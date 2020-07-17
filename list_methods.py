#!/usr/bin/env python3
'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''

if __name__ == '__main__':
    arr = []
    command_dict = {'insert': 'arr.insert(vals[0], vals[1])',
                    'remove': 'arr.remove(vals[0])',
                    'append': 'arr.append(vals[0])',
                    'sort': 'arr.sort()',
                    'reverse': 'arr.reverse()',
                    'print': 'print(arr)',
                    'pop': 'arr.pop()'}
    N = int(input())
    for _ in range(N):
        command, *line = input().split()
        vals = list(map(int, line))
        eval(command_dict[command])