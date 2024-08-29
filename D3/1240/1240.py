#1240 1일차_단순 2진 암호코드
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N X M 크기
    arr = [list(map(int,input())) for _ in range(N)]

    dic = {
        "0001101" : 0,
        "0011001" : 1,
        "0010011" : 2,
        "0111101" : 3,
        "0100011" : 4,
        "0110001" : 5,
        "0101111" : 6,
        "0111011" : 7,
        "0110111" : 8,
        "0001011" : 9
}


    for row in arr:
        print(*row)
    print()