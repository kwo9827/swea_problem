import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    a_len, b_len = map(int,input().split()) # A,B 리스트 길이
    set_A = set(map(int,input().split())) # 집합 A
    set_B = set(map(int,input().split())) # 집합 B

    if set_A == set_B:
        print("=")
    elif set_A < set_B:
        print("<")
    elif set_A > set_B:
        print(">")
    else:
        print("?")