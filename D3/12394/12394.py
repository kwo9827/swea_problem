# 12394 문자열_회문_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N = 가로세로 ,  M = 회문의 길이
    arr = [list(map(str,input())) for _ in range(N)]

    for r in range(N):   # 세로 검사
        for c in range(N-M+1): # 회문의 길이만큼
            string = arr[r][c:c+M]
            if string == string[::-1]: # 회문인지 아닌지
                print(f'#{tc}', ''.join(string))
                break

    for c in range(N):  # 가로 검사
        for r in range(N-M+1):
            string = ''
            for k in range(M):
                string += arr[r+k][c]
            if string == string[::-1]:
                print(f'#{tc} {string}')
                break



