# 1979 단어가 어디에 들어갈 수 있을까?
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    distance = 0
    cont = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                distance += 1

            if arr[i][j] == 0 or j == N-1:
                if distance == 3:
                    cont += 1
                distance = 0

    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                distance += 1

            if arr[i][j] == 0 or i == N - 1:
                if distance == 3:
                    cont += 1
                distance = 0

    print(f'#{tc} {cont}')