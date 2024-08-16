arr = [4,5,6,1,2,3,4,1,2,5,1]

# 제일 긴 루트의 기울기 구하기
# 기울기는 루트의 첫번째+마지막값  나누기 길이

start = 0
end = 0

cont = 1
max_cont = 1

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        cont += 1

        if cont > max_cont:
            max_cont = cont
            end = i
    else:
        cont = 1

long = arr[end-max_cont+1:end+1]

length = (long[0]+long[-1]) // len(long)

print(length)
print(max_cont)

