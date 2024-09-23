#21425 +=
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    x,y,N = map(int,input().split())

    cont = 0

    while x <= N and y <= N:
        if x < y:
            x += y
        else:
            y += x
        cont+=1

    print(cont)

