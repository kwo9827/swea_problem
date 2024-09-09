#IM 전등 배수
'''
- 1번부터 N번 까지 N 개의 LED 등
- i번의 배수에 해당하는 LED 등의 상태가 바뀐다.
- 원하는 패턴을 만들기 위한 최소 스위치 조작 횟수는?
- 0 : 꺼짐
- 1 : 켜짐
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [0] + list(map(int,input().split()))

    lst = [0] * len(arr)
    cont = 0

    while arr != lst:
        for i in range(1,len(arr)):
            if arr[i] != lst[i]:
                for j in range(i,len(arr),i):
                    lst[j] = 1 - lst[j]
                cont += 1

    print(f'#{tc} {cont}')


#1 3
#2 2
#3 1
#4 1
#5 8