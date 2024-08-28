from heapq import heappush, heappop, heapify

arr = [69, 10, 30, 2, 16, 8, 31, 22]
heapify(arr)
while arr:
    print(heappop(arr), end=' ')

