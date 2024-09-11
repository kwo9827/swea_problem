import sys
sys.stdin = open('input.txt')

def find_min_max(arr):
    min_val = float('inf')
    max_val = float('-inf')

    original_value = int(''.join(arr))
    min_val = min(min_val, original_value)
    max_val = max(max_val, original_value)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if i == 0 and arr[j] == '0':
                continue
            arr[i], arr[j] = arr[j], arr[i]
            value = int(''.join(arr))
            arr[i], arr[j] = arr[j], arr[i]

            min_val = min(min_val,value )
            max_val = max(max_val,value )

    return min_val, max_val

T = int(input())

for tc in range(1, T + 1):
    N = input().strip()
    arr = list(N)

    min_val, max_val = find_min_max(arr)

    print(f'#{tc} {min_val} {max_val}')
