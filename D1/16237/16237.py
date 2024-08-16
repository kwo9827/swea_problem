# 16237 배열순회_열우선
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = [[0] * 10 for _ in range(10)]
    x,y,width,height = map(int,input().split())   # x,y 좌표, width: 가로 , height : 세로
    x+=1
    y-=1

    start = 1

    for j in range(x,x+width):
        for i in range(y,y+height):
            arr[i][j] = start
            start += 1

    print(f'#{tc}')
    for row in arr:
        print(*row)