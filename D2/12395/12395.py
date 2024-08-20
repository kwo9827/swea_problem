# 12395 문자열_글자수
import sys
sys.stdin = open('input.txt')

T = int(input())
#
# for tc in range(1,T+1):
#     str1 = input()
#     str2 = input()
#
#     N = len(str1)
#     M = len(str2)
#     max_cont = 0
#
#     for i in range(N):
#         cont = 0
#         for j in range(M):
#             if str1[i] == str2[j]:
#                 cont += 1
#
#         if cont > max_cont:
#             max_cont = cont
#
#     print(f'#{tc} {max_cont}')

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    dic = {}
    max_cont = 0

    for i in str1:
        dic[i] = 0

    for j in str2:
        if j in dic:
            dic[j] += 1

    for value in dic.values():
        if value > max_cont:
            max_cont = value

    print(f'#{tc} {max_cont}')