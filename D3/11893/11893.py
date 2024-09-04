#11893 분할정복_이진탐색
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))   # 길이 N
    B = list(map(int,input().split()))   # 길이 M

    A.sort()
    B.sort()

    start = 0
    end = N
    mid = (start+end) // 2

    cont = 0
    number = 0


    while len(A) <= number:

        if A[number] <= B[mid]:
            # start =
            end = mid

        else:
            start = mid
            end = N

        for i in range(start,end):     # B에서 찾기
            pass


