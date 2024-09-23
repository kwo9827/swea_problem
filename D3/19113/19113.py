#19113 식료품 가게
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    lst = []

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] != 0:
                if arr[i] == arr[j] * 0.75:
                    lst.append(arr[i])
                    arr[j] = 0
                    break
            else:
                break

    result = ' '.join(map(str,lst))

    print(f'#{tc} {result}')