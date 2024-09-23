#13229 일요일
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    day = input()
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    result = days.index('SUN') - days.index(day)

    if result == 0:
        print(f'#{tc} 7')
    else:
        print(f'#{tc} {result}')