import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start, end):
    Q = deque([start])
    visited = set([start])

    while Q:
        string1 = Q.popleft()

        if string1 == end:
            return "Yes"

        if len(string1) < len(end):
            next_string1 = string1 + 'X'
            if next_string1 not in visited:
                Q.append(next_string1)
                visited.add(next_string1)

            next_string2 = string1[::-1] + 'Y'
            if next_string2 not in visited:
                Q.append(next_string2)
                visited.add(next_string2)

    return "No"

T = int(input())

for tc in range(1,T+1):
    S = input().strip()
    E = input().strip()

    result = BFS(S,E)

    print(f'#{tc} {result}')