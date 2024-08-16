# 1974 스도쿠 검증
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        lst = [0] * 10
        for j in range(9):
            lst[arr[i][j]] = 1
        if sum(lst) != 9:
            result = 0
            break

    for j in range(9):
        lst = [0] * 10
        for i in range(9):
            lst[arr[i][j]] = 1
        if sum(lst) != 9:
            result = 0
            break

    for i in range(1,9,3):
        lst = [0]*10
        for j in range(1,9,3):
            for r in range(3):
                for c in range(3):

                    lst[arr[r][c]] = 1
        if sum(lst) != 9:
            result = 0
            break

    print(f'#{tc} {result}')