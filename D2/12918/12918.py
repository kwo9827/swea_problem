#12918 start_이진수_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, string = input().split()

    N = int(N)
    result = []
    dic ={"A" : 10,
          "B" : 11,
          "C" : 12,
          "D" : 13,
          "E" : 14,
          "F" : 15
    }

    for i in string:
        if i in dic.keys():
            result.append(dic[i])
        else:
            result.append(int(i))

    i = len(result)-1
    lst = []
    while i >= 0:
        tar = result[i]

        for _ in range(4):
            lst.append(tar % 2)
            tar //= 2

        i -= 1
    lst.reverse()

    arr = ''.join(map(str, lst))
    print(f'#{tc} {arr}')
