#1249 4일차_보급로
import sys
sys.stdin = open('input.txt')

# def kfc(start_x,start_y,sum_val):
#     global min_val
#     if start_x == N-1 and start_y == N-1:
#         if sum_val < min_val:
#             min_val = sum_val
#         return
#
#     if sum_val > min_val:
#         return
#
#     if start_x + 1 < N:
#         kfc(start_x+1,start_y,sum_val+arr[start_x+1][start_y])
#
#     if start_y + 1 < N:
#         kfc(start_x, start_y + 1, sum_val + arr[start_x][start_y + 1])
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int,input())) for _ in range(N)]
#
#     min_val = 999999999
#
#     kfc(0,0,0)
#
#     print(f'#{tc} {min_val}')

from collections import deque

def bfs():
    global N, min_val
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((0,0))

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    while queue:
        x,y = queue.popleft()

        for k in range(4):
            nr = x + dr[k]
            nc = y + dr[k]
            if 0<= nr < N and 0<= nc < N:
                continue
            if visited[]


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    min_val = 999999999999
