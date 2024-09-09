#4008 숫자 만들기
import sys
sys.stdin = open('input.txt')

def dfs(level, tot):
    pass


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    opers = list(map(int,input().split()))
    numbers = list(map(int,input().split()))

    min_val = 1e9
    max_val = -1e9