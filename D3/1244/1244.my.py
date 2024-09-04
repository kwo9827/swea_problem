#1244 최대상금 구하기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    string, cont = input().split()
    string = list(map(str,string))
    cont = int(cont)        # 바꿀 수 있는 횟수
    visited = [[] for _ in range(cont+1)]      # 방문 장소 만들기
    N = len(string)   # 리스트 길이
    result = 0    # 결과값

    def find_max(k):
        global result
        val = int(''.join(map(str,string)))

        if val in visited[k]:
            return

        visited[k].append(val)

        if k == cont:
            result = max(result, val)

        else:
            for i in range(N-1):
                for j in range(i,N):
                    string[i],string[j] = string[j],string[i]
                    find_max(k+1)
                    string[i], string[j] = string[j], string[i]

    find_max(0)
    print(f'#{tc} {result}')