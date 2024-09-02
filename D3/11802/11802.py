#11802 완전검색_최소합
import sys
sys.stdin = open('input.txt')



def kfc(x):
    global path,N
    if x == N-1:
        print(path)
        return

    for i in range(N):
        path.append(i)
        kfc(x+1)
        path.pop()


T = int(input())

for tc in range(1,T+1):
    N = int(input())  # 가로 세로
    arr = [list(map(int,input().split())) for _ in range(N)]
    path = []
    kfc(0)