# 1215 3일차_회문1
import sys
sys.stdin = open('input.txt')

# for tc in range(1,11):
#     M = int(input())
#     arr = [list(map(str,input())) for _ in range(8)]
#     cont = 0
#     N = 8
#
#     for r in range(N):
#         for c in range(N-M+1):
#             string = arr[r][c:c+M]
#             if string == string[::-1]:
#                 cont += 1
#
#     for c in range(N):
#         for r in range(N-M+1):
#             string = ''
#             for k in range(M):
#                 string += arr[r+k][c]
#             if string == string[::-1]:
#                 cont += 1
#
#     print(f'#{tc} {cont}')

for tc in range(1,11):
    M = int(input())   # 회문의 길이
    arr = [list(input()) for _ in range(8)]
    N = 8   # 가로 세로 길이
    cont = 0

    for i in range(N):   # 가로 검사
        for j in range(N-M+1):
            Flag = True
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-k-1]:
                    Flag = False
                    break
            if Flag:    # 회문 찾으면 cont 증가
                cont += 1

    for j in range(N):  # 세로검사
        for i in range(N-M+1):
            Flag = True
            for k in range(M//2):
                if arr[i+k][j] != arr[i+M-k-1][j]:
                    Flag = False
                    break
            if Flag:   # 회문 찾으면 cont 증가
                cont+=1

    print(f'#{tc} {cont}')