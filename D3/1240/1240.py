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

    lst = ''

    new_lst = []
    for r in range(N):
        for c in range(M-1,55,-1):
            if arr[r][c] == 1:
                for k in range(c-55,c+1):
                    lst += str(arr[r][k])  # 암호 저장

    for i in range(0,56,7):   # 7자리씩 끊어서 저장
        password = ''
        for j in range(i,i+7):
            password += lst[j]
        new_lst.append(password)

    for i in range(len(new_lst)):
        new_lst[i] = dic[new_lst[i]]

    sum_val = 0

    for i in range(len(new_lst)):
        if i % 2 == 0:   # 홀수일때
            sum_val += new_lst[i] * 3

        else:   # 짝수일때
            sum_val += new_lst[i]

    if sum_val % 10 == 0:
        print(f'#{tc} {sum(new_lst)}')

    else:
        print(f'#{tc} 0')


