#2005 파스칼의 삼각형
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    arr = [[1] * N for _ in range(N)]

    arr[0][0] = 1



    for row in arr:
        print(*row)