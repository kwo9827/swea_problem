#1284 수도요금 경쟁
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())
    # P = A회사의  1L당 요금
    # S : B 회사의 1L당 초과요금  Q = R 리터 이하 요금
    # W = 한달 간 사용하는 수도 양

    min_val = 99999999

    result1 = W * P

    if W > R:
        result2 = Q + (W-R) * S

    elif W <= R:
        result2 = Q

    print(f'#{tc} {min(result1,result2)}')