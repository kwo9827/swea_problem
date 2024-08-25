#1208 1일차_Flatten
import sys
sys.stdin = open('input.txt')

# for tc in range(1,11):
#     dump = int(input())
#     arr = list(map(int,input().split()))
#
#     for _ in range(1,dump+1):
#         max_index = arr.index(max(arr))
#         min_index = arr.index(min(arr))
#         arr[max_index] -= 1
#         arr[min_index] += 1
#
#         if max(arr) - min(arr) <= 1:
#             break
#
#     print(f'#{tc} {max(arr) - min(arr)}')

for tc in range(1,11):
    dump = int(input())
    arr = list(map(int,input().split()))

    for _ in range(dump):
        max_val = float('-inf')
        min_val = float('inf')
        for i in range(len(arr)): # 현재 리스트의 최댓값,최솟값 index 구하기
            if arr[i] > max_val:
                max_val = arr[i]
                max_index = i
            if arr[i] < min_val:
                min_val = arr[i]
                min_index = i

        arr[max_index] -= 1
        arr[min_index] += 1

        if arr[max_index]-arr[min_index] <= 1:
            break

    max_val = float('-inf')
    min_val = float('inf')
    for i in range(len(arr)):  # 끝나고 나서 최대,최소 구하기
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i

    print(f'#{tc} {max_val-min_val}')


