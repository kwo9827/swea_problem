# 11611 스택2_배열최소합_확인용
import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())    # N*N 가로 세로 길이
#     arr = [list(map(int,input().split())) for _ in range(N)]   # 2차원 배열
#     min_sum = 999999999
#
#     col = []
#     for i in range(N):
#         col.append(i)
#
#     def perm(k, n, cur_sum):
#         global min_sum  # 글로벌 선언
#         if min_sum <= cur_sum:  # 합을 더하는 중에 이미 존재하는 최솟값보다 작으면 멈춤
#             return  # 가지치기
#
#         if k == n:  # 행과 열을 다 돌았으면
#             min_sum = cur_sum
#
#         else:
#             for i in range(k, n):
#                 col[k],col[i] = col[i],col[k]
#                 perm(k+1,n,cur_sum+arr[k][col[k]])  # cur_sum에 더해줌
#                 col[k],col[i] = col[i],col[k]
#
#     perm(0,N,0)
#
#     print(f'#{tc} {min_sum}')

T = int(input())

for tc in range(1,T+1):
    N = int(input())    # N*N 가로 세로 길이
    arr = [list(map(int,input().split())) for _ in range(N)]   # 2차원 배열
    min_sum = 999999999

    used = [0] * N    # 지나온지 안 지나온지 확인하기

    def perm(k,cur_sum):
        global min_sum
        if min_sum <= cur_sum:  # 가지치기
            return
        if k == N:   # 모든 행과 열을 돌았으면 멈춘다
            min_sum = cur_sum
        else:
            for i in range(N): # 0,1,2 까지만
                if used[i]:
                    continue
                used[i] = 1
                perm(k+1,cur_sum + arr[k][i])
                used[i] = 0

    perm(0,0)

    print(f'#{tc} {min_sum}')