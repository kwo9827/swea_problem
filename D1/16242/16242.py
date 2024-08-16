# 16242 배열순회_지그재그
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    x,y,width,height = map(int,input().split())
    arr = [[0] * 10 for _ in range(10)]

    start = 1
    for i in range(x,x+height):
        if i%2 != 0:
            for j in range(y,y+width):
                arr[i][j] = start
                start+=1

        else:
            for j in range(y+width-1,y-1,-1):
                arr[i][j] = start
                start+=1


    print(f'#{tc}')
    for row in arr:
        print(*row)