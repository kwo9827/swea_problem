# 20397 돌 뒤집기 게임 2
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        i,j = map(int,input().split())
        i -= 1   # 리스트 인덱스는 0부터 시작하므로

        for k in range(1,j+1):
            left = i - k     # i기준으로 k칸 왼쪽
            right = i + k    # i기준으로 k칸 오른쪽

            if left < 0 or right >= N:
                break

            if arr[left] == arr[right]:  # 왼쪽 오른쪽 색이 같으면
                arr[left] = 1 - arr[left]  # 1-1=0 , 1-0=1  -> 숫자가 바뀌게 된다.
                arr[right] = 1 - arr[right]

    print(f'#{tc}',*arr)
