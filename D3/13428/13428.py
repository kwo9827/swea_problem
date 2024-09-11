#13428
import sys
sys.stdin = open('input.txt')

def find_min_max(arr):
    global min_val, max_val, value

    min_val = min(min_val, value)
    max_val = max(max_val, value)

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i == 0 and arr[j] == 0:
                continue
            arr[i],arr[j] = arr[j],arr[i]
            value = int(''.join(map(str,arr)))
            arr[j],arr[i] = arr[i],arr[j]

            min_val = min(min_val, value)
            max_val = max(max_val,value)

    return min_val, max_val

T = int(input())

for tc in range(1,T+1):
    arr = list(map(int,input()))

    value = int(''.join(map(str,arr)))

    max_val = float('-inf')
    min_val = float('inf')

    min_val, max_val = find_min_max(arr)

    print(f'#{tc} {min_val} {max_val}')

