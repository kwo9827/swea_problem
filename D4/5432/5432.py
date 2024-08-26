#5432 쇠막대기 자르기
import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1,T+1):
#     string = list((input()))
#     N = len(string)   # 길이
#
#     cont = 0   # 잘린 쇠막대기 수
#     # 레이저를 만나면 레이저 수 + 1 만큼 증가함
#
#     for i in range(1,N):
#         if string[i-1] == "(":
#             if string[i] == ")":
#                 string[i-1],string[i] = 1,2  # 레이저 표시
#
#     lst = []   # 괄호를 넣을 리스트
#
#     for i in range(N):        # ( 을 만나면 리스트에 넣고 닫는 괄호를 만나면 인덱스 값을 저장함
#         if string[i] == '(':
#             lst.append((string[i],i))   # 값과 인덱스 번호를 같이 저장
#             string[i] = 0
#
#         elif string[i] == ')':  # ')'를 만나면
#             if lst[-1][0] == '(':  # 마지막 값이 '('이면
#                 start_idx = lst[-1][1]  # 시작 인덱스와 끝 인덱스 추출
#                 lst.pop(-1)   # 리스트에서 제거
#                 string[i] = 0  # 0으로 바꿔줌
#                 end_idx = i
#
#                 raser = 0
#
#                 for k in range(start_idx, end_idx):  # 지정한 범위에서 레이저를 만나면
#                     if string[k] == 1:
#                         raser += 1
#
#                 cont += raser + 1  # 쇠막대기 수는 레이저 개수 + 1
#
#     print(f'#{tc} {cont}')

T = int(input())

for tc in range(1,T+1):
    string = list(input())
    N = len(string)
    stack = []
    cont = 0

    i= 0
    while i < N:
        if string[i] == '(':  # 레이저를 만나면 스택 길이만큼
            if string[i+1] == ')':
                cont += len(stack)
                i += 1

            else:
                stack.append(string[i])

        else:
            stack.pop()
            cont += 1

        i+=1

    print(f'#{tc} {cont}')