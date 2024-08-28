#1232 9일차_사칙연산
import sys
sys.stdin = open('input.txt')


def bst(v):
    # 노드가 없는 경우 리턴
    if v > N or tree[v] == 0:
        return 0

    # 현재 노드가 연산자인 경우
    if tree[v] in '+-*/':
        # 왼쪽 서브트리 계산
        left_result = bst(left[v])
        # 오른쪽 서브트리 계산
        right_result = bst(right[v])

        # 연산자에 따라 계산 수행
        if tree[v] == '+':
            return left_result + right_result
        elif tree[v] == '-':
            return left_result - right_result
        elif tree[v] == '*':
            return left_result * right_result
        elif tree[v] == '/':
            return left_result / right_result
    else:
        # 숫자인 경우 해당 값을 리턴
        return float(tree[v])


for tc in range(1, 11):
    N = int(input())  # 노드의 개수
    tree = [0] * (N + 1)  # 노드의 값을 저장할 리스트
    left = [0] * (N + 1)  # 왼쪽 자식 노드를 저장할 리스트
    right = [0] * (N + 1)  # 오른쪽 자식 노드를 저장할 리스트

    for _ in range(N):
        arr = input().split()
        idx = int(arr[0])  # 노드 번호
        tree[idx] = arr[1]  # 노드 값 (연산자 또는 숫자)

        # 자식 노드가 있는 경우 저장
        if len(arr) > 2:
            left[idx] = int(arr[2])
        if len(arr) > 3:
            right[idx] = int(arr[3])

    # 루트 노드에서부터 결과 계산
    result = bst(1)
    print(f'#{tc} {int(result)}')  # 결과는 정수로 출력

