#7465 창용 마을 무리의 개수
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # -----------------------------------------
    # 정점 번호: 1 ~ V
    p = []
    for i in range(V+1):
        p.append(i)
    # x가 속한 집합(트리)의 대표자(루트)를 반환
    def find_set(x):
        if x == p[x]:
            return x
        else:
            p[x] = find_set(p[x])
            return p[x]
    # -----------------------------------------
    ans = V
    for _ in range(E):
        u, v = map(int, input().split())
        a = find_set(u)
        b = find_set(v)
        if a == b:
            continue
        p[a] = b
        ans -= 1

    print(f'#{tc} {ans}')