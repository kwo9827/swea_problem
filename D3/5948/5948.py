# 5948 새샘이의 7-3-5 게임
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = list(map(int,input().split()))

    x = 3
    path = []
    lst = []

    def kfc(level, cur_place):
        if x == level:
            lst.append(sum(path))
            return

        for i in range(cur_place, len(arr)):
            path.append(arr[i])
            kfc(level+1, i + 1)
            path.pop()

    kfc(0, 0)

    lst.sort()
    result = list(set(lst))
    print(f'#{tc} {result[-5]}')
