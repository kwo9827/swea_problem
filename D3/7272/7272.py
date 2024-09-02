#7272 안경이 없어
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    string1, string2 = map(str,input().split())
    lst1 = ['A','D','O','P','Q','R']
    lst2 = ['B']

    N = len(string1)   # 1번 길이
    M = len(string2)   # 2번 길이

    Flag = True
    i = 0

    if N != M:
        print(f'#{tc} DIFF')
    else:
        while i < N:
            if string1[i] in lst1 and string2[i] in lst1:
                Flag = True
            elif string1[i] in lst2 and string2[i] in lst2:
                Flag = True
            else:
                if string1[i] not in lst1 and string2[i] not in lst1 and string1[i] not in lst1 and string2[i] not in lst2:
                    Flag = True
                else:
                    print(f'#{tc} DIFF')
                    Flag = False
                    break
            i += 1

        if Flag == True:
            print(f'#{tc} SAME')

