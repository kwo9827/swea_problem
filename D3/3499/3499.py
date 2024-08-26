#3499 퍼펙트셔플
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(input().split())

    R = N//2

    new_arr = []

    if N % 2 != 0:   # N이 홀수면
        left_arr = arr[:R+1]   # 범위를 1 더해서 왼쪽이 하나 더 많게 해줌
        right_arr = arr[R+1:]

        for i in range(R):
            new_arr.append(left_arr[i])
            new_arr.append(right_arr[i])
        new_arr.append(left_arr[-1])   # 마지막에는 왼쪽 리스트에 하나가 남을꺼니깐

    else:
        left_arr = arr[:R]
        right_arr = arr[R:]

        for i in range(R):
            new_arr.append(left_arr[i])
            new_arr.append(right_arr[i])

    result = ' '.join(new_arr)

    print(f'#{tc} {result}')

