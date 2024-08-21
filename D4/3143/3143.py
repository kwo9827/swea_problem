# 3143 가장 빠른 문자열 타이핑
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    A,B = map(str,input().split())
    cont = 0

    N = len(A)  # 긴거
    M = len(B)  # 짧은거

    i = 0
    while i <= N-M:
        if A[i:i+M] == B:
            cont += 1
            i += M
        else:
            cont+=1
            i+=1

    cont += N-i

    print(f'#{tc} {cont}')