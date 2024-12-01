## 라이브러리 사용 X
n = int(input())
n_list = list(map(int,input().split()))

max_value = n_list[0]
for i in range(n):
    if max_value <= n_list[i]:
        max_value = n_list[i]

fixed_list = [n_list[i]/max_value*100 for i in range(n)]
result = 0
for i in range(n):
    result += fixed_list[i]

print(result/n)

## 라이브러리 사용O
n = int(input())
n_list = list(map(int,input().split()))

max_value = max(n_list)

fixed_list = [(score/max_value)*100 for score in n_list]
new_average = sum(fixed_list)/n

print(new_average)