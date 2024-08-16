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
    for c in range(5):
        for r in range(15):
            if lst[r][c]==-1:
                continue
            else:
                words.append(lst[c][r])

    print(words)

