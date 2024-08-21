# 1216 3일차_회문2
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    N = 100  # 가로 세로 길이
    result = 0

    for M in range(100,1,-1):  # 거꾸로 확인
        for i in range(N):  # 가로 검사
            for j in range(N-M+1):
                Flag = True    # 회문 찾았는지 확인용
                for k in range(M//2):
                    if arr[i][j+k] != arr[i][j+M-k-1]:
                        Flag = False
                        break

                if Flag:   # 회문 찾았으면 result에 길이 저장
                    result = M
                    break
            if Flag:
                break
        if Flag:
            break

        for j in range(N):  # 세로 검사
            for i in range(N-M+1):
                Flag = True
                for k in range(M//2):
                    if arr[i+k][j] != arr[i+M-k-1][j]:
                        Flag = False
                        break

                if Flag:
                    result = M
                    break
            if Flag:
                break
        if Flag:
            break

    print(f'#{tc} {result}')
