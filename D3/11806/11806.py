#11806 탐욕_베이비진 게임
import sys
sys.stdin = open('input.txt')

def check_winner(cards):
    for i in range(len(cards)): # triplet 검사
        if cards[i] == 3:
            return True

    for i in range(len(cards) - 2):  # run 검사
        if cards[i] >= 1 and cards[i + 1] >= 1 and cards[i + 2] >= 1:
            return True
    return False

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    player1_card = [0] * 10  # 각 숫자 카드의 개수를 저장할 리스트
    player2_card = [0] * 10  # 각 숫자 카드의 개수를 저장할 리스트

    winner = 0

    for i in range(len(arr)):
        if i % 2 != 0:
            player2_card[arr[i]] += 1

            if check_winner(player2_card):
                winner = 2
                break
        else:
            player1_card[arr[i]] += 1

            if check_winner(player1_card):
                winner = 1
                break

    print(f'#{tc} {winner}')