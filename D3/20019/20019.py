#20019 회문의 회문
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = input()

    N = len(arr)
    mid = N // 2

    for i in range(mid):
        if arr[i] == arr[N-i-1]:
            Flag = True
        else:
            Flag = False
            break

    if Flag:
        if arr[mid+1:] == arr[:mid]:
            print(f'#{tc} YES')

        else:
            print(f'#{tc} NO')

    else:
        print(f'#{tc} NO')

