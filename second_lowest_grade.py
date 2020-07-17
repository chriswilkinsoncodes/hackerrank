#!/usr/bin/env python3

def get_runners_up1(grades):
    grades.sort(key=lambda x: x[1])
    lowest = grades.pop(0)[1]
    while grades[0][1] == lowest:
        grades.pop(0)
    second_lowest = grades[0][1]
    while grades and grades[0][1] == second_lowest:
        runners_up.append(grades.pop(0)[0])
    return runners_up

def get_runners_up(grades):
    scores = {grades[i][1] for i in range(len(grades))}
    scores.remove(min(scores))
    return [grades[i][0] for i in range(len(grades)) if grades[i][1] == min(scores)]
     

if __name__ == '__main__':
    grades = []
    runners_up = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
    
    for runner_up in sorted(get_runners_up(grades)):
        print(runner_up)