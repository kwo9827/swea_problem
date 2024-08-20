# 1213 3_String
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    T = int(input())
    str1 = input()
    str2 = input()
    cont = 0
    N = len(str1)  # 짧은거
    M = len(str2)  # 긴거

    for i in range(M-N+1):
        if str2[i:i+N] == str1:
            cont+=1

    print(f'#{T} {cont}')