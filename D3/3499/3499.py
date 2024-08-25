#3499 퍼펙트셔플
import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # 카드 개수 N 입력 받기
    N = int(input())
    # 카드 덱 입력 받기
    cards = input().split()

    # 덱을 절반으로 나누기
    if N % 2 == 0:
        left_half = cards[:N // 2]
        right_half = cards[N // 2:]
    else:
        left_half = cards[:(N // 2) + 1]
        right_half = cards[(N // 2) + 1:]

    # 퍼펙트 셔플 수행
    shuffled_deck = []
    for i in range(len(right_half)):
        shuffled_deck.append(left_half[i])
        shuffled_deck.append(right_half[i])

    # 홀수인 경우 남은 한 장을 추가
    if len(left_half) > len(right_half):
        shuffled_deck.append(left_half[-1])

    # 결과 출력
    print(f"#{test_case} {' '.join(shuffled_deck)}")

