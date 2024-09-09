# 고대유적2
import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for r in range(N):
        for c in range(M):
            cnt = 0
            if arr[r][c] == 1:
                nr = r
                nc = c
                while nr<N and nc <M and arr[nr][nc] == 1:
                    nr += 1
                    cnt += 1
                if ans <= cnt:
                    ans = cnt
                cnt = 0

            if arr[r][c] == 1:
                nr = r
                nc = c
                while nr<N and nc <M and arr[nr][nc] == 1:
                    nc += 1
                    cnt += 1
                if ans <= cnt:
                    ans = cnt
                cnt = 0
    print(ans)
