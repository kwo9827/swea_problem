import sys
sys.stdin = open('input.txt')

def horae(left,right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]

    arr[left],arr[j] = arr[j],arr[left]

    return j

def quick(left,right):
    if left < right:
        pivot = horae(left,right)
        quick(left,pivot-1)
        quick(pivot+1,right)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    quick(0,N-1)

    print(f'#{tc} {arr[N//2]}')