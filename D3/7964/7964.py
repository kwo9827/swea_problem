import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())
    cities = list(map(int, input().split()))

    count = 0
    i = 0

    while i < N:
        if cities[i] == 1:
            i += 1
        else:
            # 0이 연속된 구간 시작
            j = i
            while j < N and cities[j] == 0:
                j += 1

            gap = j - i  # 연속된 0의 개수
            count += (gap + D - 1) // D  # D칸마다 하나씩 설치
            i = j  # 0 구간 끝까지 스킵

    print(f"#{tc} {count}")
