arr = [69, 10, 30, 2, 16, 8, 32, 21]


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) >> 1  # len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    # 병합
    ret = []  # left + right를 정렬된 상태로 합쳐서 저장
    while left and right:  # left나 right 중에 하나라도 텅 비어있게 될 때까지 반복
        if left[0] < right[0]:
            ret.append(left.pop(0))
        else:
            ret.append(right.pop(0))

    # 아직 리스트에 남아있는 원소들 있다면 마저 ret에 넣어주기
    ret.extend(left)  # ret + left
    ret.extend(right)  # ret + right

    return ret


print(arr)
sorted_lst = merge_sort(arr)
print(sorted_lst)