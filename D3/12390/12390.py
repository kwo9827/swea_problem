# 12390 배열2_부분집합의합_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 부분집합의 원소 수, K: 부분집합의 합
    lst = list(range(1, 13))  # 1~12 리스트
    total_count = 0  # 총개수

    def perm(k, cur_sum, count):
        global total_count
        if count > N or cur_sum > K:  # 가지치기: 원소의 수가 N을 넘거나 합이 K를 넘으면 종료
            return
        if count == N and cur_sum == K:  # 원소의 수가 N이고 합이 K인 경우
            total_count += 1
            return

        if k >= 12:  # 더 이상 고려할 원소가 없을 때 종료
            return

        # 원소를 선택하는 경우
        perm(k + 1, cur_sum + lst[k], count + 1)
        # 원소를 선택하지 않는 경우
        perm(k + 1, cur_sum, count)

    perm(0, 0, 0)  # 첫번째 원소, 합 0, 원소 수 0
    print(f'#{tc} {total_count}')
