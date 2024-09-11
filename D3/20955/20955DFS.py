#20955 XY 문자열1
import sys
sys.stdin = open('input.txt')

def dfs(start, end):
    if len(start) == len(end):
        if start == end:
            return "Yes"
        else:
            return "No"


    if len(start) < len(end):
        result1 = dfs(start + 'X', end)
        if result1 == 'Yes':
            return "Yes"

        result2 = dfs(start[::-1] + 'Y', end)
        if result2 == 'Yes':
            return "Yes"

    return "No"

T = int(input())

for tc in range(1,T+1):
    S = input()
    E = input()

    result = dfs(S,E)

    print(result)
