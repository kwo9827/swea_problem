# 의석이의 세로로 말해요
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):

    lst = []
    for _ in range(5):
        arr = list(input())
        arr += [-1] * (15-len(arr))
        lst.append(arr)

    words =[]
    for c in range(15):
        for r in range(5):
            if lst[r][c]==-1:
                continue
            else:
                words.append(lst[r][c])

    result = ''.join(words)
    print(f'#{tc} {result}')

