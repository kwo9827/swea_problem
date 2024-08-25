#12386 배열1_숫자카드_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    str1 = input()
    lst = [0] * 101  # 최대 101개

    for i in str1:
        lst[int(i)] += 1

    max_val = 0

    for i in range(len(lst)):
        if lst[i] >= max_val:
            max_val = lst[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_val}')




