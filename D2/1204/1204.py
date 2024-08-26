#1204 최빈수 구하기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    t = int(input())
    arr = list(map(int,input().split()))
    lst = [0] * 101

    max_val = 0

    for i in range(len(arr)):
        lst[arr[i]] += 1

    for i in range(len(lst)):
        if lst[i] >= max_val:
            max_val = lst[i]
            max_idx = i

    print(f'#{tc} {max_idx}')