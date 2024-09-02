path = []
arr = list(map(int,input().split())) # 235777

def kfc(x):
    if x == 6:
        if baby_gin(path):
            print("Baby Gin!")
        return

    for i in arr:
        path.append(i)
        kfc(x+1)
        path.pop()

def baby_gin(path):
    counts = [0] * 10
    for num in path:
        counts[num] += 1

    triplet = 0
    run = 0

    i = 0
    while i < 10:
        if counts[i] >= 3:  # 트리플 체크
            triplet += 1
            counts[i] -= 3
            continue

        if i <= 7 and counts[i] >= 1 and counts[i+1] >= 1 and counts[i+1] >= 1:  # 런 체크
            run += 1
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            continue

        i += 1

    return triplet + run == 2

kfc(0)
