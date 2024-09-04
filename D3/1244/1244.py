#1244 최대 상금
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    nums, swap_cnt = input().split()
    nums = list(map(int, nums))
    swap_cnt = int(swap_cnt)       # 바꿀 수 있는 횟수
    N = len(nums)      # 길이
    visit = [[] for _ in range(swap_cnt + 1)]
    ans = 0

    def find_max(k):
        global ans
        val = int(''.join(map(str, nums)))

        if val in visit[k]:
            return

        visit[k].append(val)

        if k == swap_cnt:
            ans = max(ans, val)

        else:
            for i in range(N -  1):
                for j in range(i + 1, N):
                    nums[i], nums[j] = nums[j], nums[i]
                    # ==========================================
                    find_max(k + 1)
                    # ==========================================
                    nums[i], nums[j] = nums[j], nums[i]

    find_max(0)
    print(f'#{tc} {ans}')
