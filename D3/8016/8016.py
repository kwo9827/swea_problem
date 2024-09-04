#8016 홀수 피라미드
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    num = N    # 시작 N
    lst = []
    cont = 0
    start = 1


