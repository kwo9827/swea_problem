# 1221 GNS
import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1,T+1):
#     test_case, N = map(str,input().split())
#     arr = list((input().split()))
#     N = int(N)
#     lst = [0] * 10
#     dic = {'ZRO' : 0 ,'ONE' : 0,'TWO' : 0,'THR' : 0,'FOR' : 0,'FIV' :0 ,
#            'SIX': 0,'SVN': 0,'EGT': 0,'NIN': 0}
#
#     for i in arr:
#         dic[i] += 1
#
#     print(test_case)
#     for key in dic:
#         print((key + ' ')*dic[key],end = '')

T = int(input())

for tc in range(1,T+1):
    test_case, N = map(str,input().split())
    arr = list(map(str,input().split()))
    lst = [0] * 10
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in arr:
        lst[number.index(i)] += 1

    print(test_case)
    for i in range(len(lst)):
        print((number[i]+ ' ') * lst[i], end = '')