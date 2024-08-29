#12919 start_이진수2_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = float(input())

    lst = []
    cont = 0

    while cont <= 13:
        num = N * 2

        if num > 1:
            num -= 1
            lst.append(1)

        elif num == 1:
            lst.append(1)
            break

        else:
            lst.append(0)

        N = num
        cont += 1

    result = ''.join(map(str,lst))

    if len(lst) >= 13:
        print(f'#{tc}', "overflow")

    else:
        print(f'#{tc} {result}')






