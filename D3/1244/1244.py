#1244 최대 상금
import sys
sys.stdin = open('input.txt')

def kfc(string,N,cur_val):
    global max_val, cont
    if cont == N:
        return

    for i in range(len(string)):
        pass


T = int(input())

for tc in range(1,T+1):
    string, N = map(str,input().split())  # string = 숫자열,  N = 변경하는 횟수
    N = int(N)
    max_val = 0
    visited = [0]*len(string)
    cont = 0  # 시도 횟수

    kfc(0,0,0)

    print(f'#{tc} {max_val}')