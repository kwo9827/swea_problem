#12399 스택1_반복문자 지우기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    N = len(str1)   # str1 길이
    stack = [0] * N

    top = -1
    cont=  0

    for i in range(N):
        if str1[i] == stack[top]:
            stack[top] = 0
            top -= 1

        else:
            top+=1
            stack[top] = str1[i]

    for j in range(len(stack)):
        if stack[j] != 0:
            cont +=1

    print(f'#{tc} {cont}')



