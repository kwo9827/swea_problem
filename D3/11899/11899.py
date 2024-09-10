#11899 그래프_그룹나누기
import sys
sys.stdin = open('input.txt')


# x가 속한 집합(트리)의 대표자(루트)를 반환
def find_set(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # -----------------------------------------
    # 정점 번호: 1 ~ V
    p = []
    for i in range(V+1):
        p.append(i)
    # -----------------------------------------

    ans = V

    arr = list(map(int,input().split()))
    for i in range(E):
        u,v = arr[i*2],arr[i*2+1]

        a = find_set(u)
        b = find_set(v)
        if a == b:  # 부모가 연결되어 있으면
            continue
        p[a] = b
        ans -= 1

    print(f'#{tc} {ans}')
