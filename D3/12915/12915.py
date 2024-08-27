#12915 트리_이진탐색_확인용
import sys
sys.stdin = open('input.txt')

def dfs(v):
    if v == 0:
        return

    dfs(L[v])
    print(v, end = '')
    dfs(R[v])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 노드 리스트 생성 (1부터 N까지)
    lst = list(range(1, N + 1))

    # 이진 트리의 구조를 위한 배열 초기화
    L = [0] * (N + 1)  # 왼쪽 자식
    R = [0] * (N + 1)  # 오른쪽 자식
    P = [0] * (N + 1)  # 부모

    # 이진 트리 구성
    for i in range(1, N // 2 + 1):
        if 2 * i <= N:
            L[i] = 2 * i  # 왼쪽 자식
            P[2 * i] = i  # 부모 설정
        if 2 * i + 1 <= N:
            R[i] = 2 * i + 1  # 오른쪽 자식
            P[2 * i + 1] = i  # 부모 설정

    # 결과 출력
    print(f'#{tc}')
    print('왼쪽 자식:', L)
    print('오른쪽 자식:', R)
    print('부모:', P)

    dfs(N)


