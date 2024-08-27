T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 격자 크기, M = 폭탄 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, -1, 0, 1]  # 우, 상, 좌, 하
    dc = [1, 0, -1, 0]
    total_sum = 0

    for _ in range(M):
        r1, c1, bomb = map(int, input().split())

        # 폭탄이 떨어진 위치의 적군 수 추가
        total_sum += arr[r1][c1]
        arr[r1][c1] = 0  # 이미 합산된 위치는 0으로 설정

        # 폭발 범위 계산
        for k in range(4):  # 4방향
            for i in range(1, bomb + 1):  # 폭발력에 따른 거리
                nr = r1 + dr[k] * i
                nc = c1 + dc[k] * i

                # 배열 범위 내의 인덱스인지 확인
                if 0 <= nr < N and 0 <= nc < N:
                    total_sum += arr[nr][nc]
                    arr[nr][nc] = 0  # 이미 합산된 위치는 0으로 설정

    print(f'#{tc} {total_sum}')