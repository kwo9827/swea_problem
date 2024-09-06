import sys
sys.stdin = open('input.txt')

def kfc(distance,cont):
    global min_cont
    if distance >= len(M):
        if cont < min_cont:
            min_cont = cont
        return

    if cont > min_cont:
        return

    for i in range(1,M[distance] + 1):
        kfc(distance + i, cont + 1)


T = int(input())

for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr.pop(0)
    M = arr

    min_cont = 99999999
    kfc(0,0)

    print(f'#{tc} {min_cont - 1}')

