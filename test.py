import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    string = list(input().strip())
    N = len(string)  # 문자열 길이

    stack = []
    total_pieces = 0

    i = 0
    while i < N:
        if string[i] == '(':
            # 레이저인지 쇠막대기 시작인지 판별
            if string[i + 1] == ')':  # 레이저일 경우
                total_pieces += len(stack)  # 현재 스택에 쌓여있는 쇠막대기 개수만큼 더하기
                i += 1  # 레이저이기 때문에 다음 괄호로 넘기기
            else:
                stack.append('(')  # 쇠막대기 시작
        else:
            stack.pop()  # 쇠막대기 끝
            total_pieces += 1  # 쇠막대기 끝을 만나면 조각 수 1 증가
        i += 1

    print(f'#{tc} {total_pieces}')