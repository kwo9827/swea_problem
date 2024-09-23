#18662 등차수열 만들기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    a,b,c = map(int,input().split())

    value = abs((a+c)/2 - b)

    if b - a == c - b:
        print(f'#{tc} 0.0')

    else:
        print(f'#{tc} {value}')
