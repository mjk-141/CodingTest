N = int(input())
n_list = list(map(int, input().split()))
sum = 0
for num in n_list:
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if num != 1 and cnt == 2:
        sum += 1
print(sum)
