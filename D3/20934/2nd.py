import sys
sys.stdin = open('input.txt')

T = int(input())
ans_lst = []

for tc in range(1,T+1):
    string, K = map(str,input().split())
    string = list(string)

    K = int(K)
    i = 1

    while K != 0:

        string[i], string[i-1] = string[i-1], string[i]

        i += 1
        K -= 1

    for i in range(len(string)):
        if string[i] == 'o':
            ans_lst.append(f'#{tc} {i}\n')

print(''.join(ans_lst))
