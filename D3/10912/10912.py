#10912 외로운 문자
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = list(input())  # 리스트로 받기

    lst = []  # 빈 리스트 생성

    for i in range(len(arr)):
        if arr[i] not in lst:
            lst.append(arr[i])

        else:
            a = lst.index(arr[i])
            lst.pop(a)

    lst.sort()
    result = ''.join(lst)

    if len(lst) == 0:
        print(f'#{tc}', "Good")

    else:
        print(f'#{tc} {result}')






