

arr = [(6, 0), (3, 3), (-7, 2), (-4, -1)]  # 지렁이들의 좌표
N = len(arr) // 2  # 매칭할 쌍의 수

def kfc(start, level, used, path):
    if level == N:  # 필요한 쌍을 다 골랐다면
        remaining = [arr[i] for i in range(len(arr)) if not used[i]]  # 남은 지렁이들
        path.append(remaining)  # 남은 지렁이들로 만들어진 쌍 추가
        print(path)  # 현재 매칭된 쌍들을 출력
        path.pop()
        return

    for i in range(start, len(arr)):
        if not used[i]:
            for j in range(i + 1, len(arr)):
                if not used[j]:
                    # i와 j를 매칭시키고
                    used[i] = used[j] = True
                    path.append([arr[i], arr[j]])
                    kfc(i + 1, level + 1, used, path)
                    # 백트래킹: 선택 취소
                    path.pop()
                    used[i] = used[j] = False

used = [False] * len(arr)
kfc(0, 0, used, [])