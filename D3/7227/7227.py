#7227 사랑의 카운슬러
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    for _ in range(N):
        x,y = map(int,input().split())