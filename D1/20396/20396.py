#20396 돌 뒤집기 게임1
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        i,j = map(int,input().split())
        i -= 1

        for k in range(i,min(i+j,N)):
            arr[k] = arr[i]

    print(f'#{tc}', *arr)