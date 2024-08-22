T = int(input())

for tc in range(1, T + 1):
    string = input()
    stack = [0] * len(string)
    top = -1
    value = 1
    dic = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for i in range(len(string)):
        if string[i] in dic.keys():  # dic key가 string 안에 있으면 그 값을 stack 에 추가
            top += 1
            stack[top] = string[i]
            # print(stack)

        elif string[i] in dic.values():  # dic value가 string 안에 있으면
            # top +=1
            # stack[top] = string[i]
            # print(stack)
            if top >= 0 and dic[stack[top]] == string[i]:  # stack이 비어있지 않고 짝이 맞는다면
                stack[top] = 0  # 해당 스택값 0으로 바꿈
                top -= 1
                # print(stack)
            else:
                value = 0

    if top >= 0:  # stack이 비어 있지 않으면 0을 반환
        value = 0

    print(f'#{tc} {value}')