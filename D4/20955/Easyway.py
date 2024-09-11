import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    S = list(input())
    E = list(input())

    while len(E) > len(S):
        if E[-1] == 'X':
            E.pop()
        else:
            E.pop()
            E.reverse()

    if S == E:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')