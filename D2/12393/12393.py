# 12393 문자열_문자열비교_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N = len(str1)   # str1이 str2보다 짧음
    M = len(str2)
    result = 0

    for i in range(M-N+1):
        if str1[0] == str2[i]:
            if str1 == str2[i:i+N]:
                result = 1
                break

    print(f'#{tc} {result}')