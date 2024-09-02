#11803 완전검색_전자카트
import sys
sys.stdin = open('input.txt')

path = []

def kfc(x):
    global N,path
    if x == N:
        print(path)
        return

    for i in range(3):
        path.append(i)
        kfc(x+1)
        path.pop()



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_sum = 999999

    for row in arr:
        print(*row)

    kfc(1)
