#12741 두 전구
import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1, T + 1):
#     A1, A2, B1, B2 = map(int, input().split())
#
#     lst = [0] * 50000
#     cont = 0
#
#     for i in range(A1,A2):
#         lst[i] += 1
#     for i in range(B1,B2):
#         lst[i] += 1
#
#     for i in range(len(lst)):
#         if lst[i] == 2:
#             cont += 1
#
#     print(f'#{tc} {cont}')

T = int(input())

lst = []

for tc in range(1,T+1):
    A1,A2,B1,B2 = map(int,input().split())

    start = max(A1,B1)
    end = min(A2,B2)

    result = end - start

    if result <= 0:
        result = 0

    lst.append(result)

for index,result in enumerate(lst):
    print(f'#{index+1} {result}')