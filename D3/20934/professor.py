import sys
sys.stdin = open('input.txt')

T = int(input())
ans_lst = []

for tc in range(1, T + 1):
    arr, K = input().split()
    K = int(K)
    pos = arr.index('o')
    ans = 0
    if K == 0:
        ans = pos
    elif pos != 1:
        ans = 1 if K % 2 else 0
    else:
        ans = 0 if K % 2 else 1

    ans_lst.append(f'#{tc} {ans}\n')

print(''.join(ans_lst))