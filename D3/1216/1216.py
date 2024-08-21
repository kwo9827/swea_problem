# 1216 3일차_회문2
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())  # 테스트 케이스 번호 입력
    arr = [input() for _ in range(100)]  # 100x100 글자판 입력
    max_len = 0  # 가장 긴 회문의 길이를 저장할 변수 초기화

    # 가로 방향으로 회문 탐색
    for i in range(100):  # 각 행에 대해
        for j in range(100):  # 각 열에서 시작 위치
            for k in range(j+1,101):  # 부분 문자열의 끝 위치 // 회문의 길이
                string = arr[i][j:k]  # 현재 행에서 부분 문자열 추출
                if string == string[::-1]:  # 회문인지 확인
                    if len(string) > max_len:
                        max_len = len(string)

    # 세로 방향으로 회문 탐색
    for j in range(100):  # 각 열에 대해
        for i in range(100):  # 각 행에서 시작 위치
            for k in range(i+1,101):  # 부분 문자열의 끝 위치
                string = ''  # 세로 방향 문자열 초기화
                for l in range(i, k):  # 세로 방향으로 문자열 구성
                    string += arr[l][j]
                if string == string[::-1]:  # 회문인지 확인
                    if len(string) > max_len:  # 더 긴 회문이면
                        max_len = len(string)  # 최대 길이 갱신

    # 결과 출력
    print(f'#{T} {max_len}')



