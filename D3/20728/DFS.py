#20728 공편한 분배2
import sys
sys.stdin = open('input.txt')

ans_lst = []

def kfc(level,start):
    global path, min_val
    if level == K:
        min_val = min(min_val, max(path)-min(path))
        return

    for i in range(start,N):
        path.append(arr[i])
        kfc(level+1, i+1)
        path.pop()

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

    min_val = 999999999

    path = []
    kfc(0,0)

    ans_lst.append(f'#{tc} {min_val}\n')

print(''.join(ans_lst))