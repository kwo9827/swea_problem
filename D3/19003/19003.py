#19003 팰린드롬 문제
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    for _ in range(N):
        string = input()