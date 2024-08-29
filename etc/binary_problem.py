arr = '0000000111100000011000000111100110000110000111100111100111111001100111'
lst= []
N = len(arr) // 7
start_pos = 0
# for i in range(N):
#     lst.append(arr[start_pos:start_pos+7])
#     start_pos = start_pos+7

for s in range(0,len(arr),7):
    lst.append(arr[s:s+7])

result = []  # 변환 숫자를 담을 리스트
i = 0

while i < len(lst):
    tar = lst[i]
    num = 0

    for j in range(7):
        num += (2**(6-j)) * int(tar[j])

    result.append(num)
    i += 1

print(*result)
