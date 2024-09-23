#20934 방울 마술
import sys
sys.stdin = open('input.txt')

T = int(input())
ans_lst = []

for tc in range(1,T+1):
    arr, K = input().split()
    K = int(K)
    pos = arr.index('o')
    result = 0

    if K == 0:
        result = pos

    elif pos != 1:
        if K % 2 == 0:
            result = 0
        else:
            result = 1

    else:
        if K % 2 == 0:
            result = 1
        else:
            result = 0

    ans_lst.append(f'#{tc} {result}\n')

print(''.join(ans_lst))

