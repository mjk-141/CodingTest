# 라이브러리 사용 안할시
n_list = []

for i in range(9):
    n = int(input())
    n_list.append((n, i+1))

max_value,max_index = n_list[0]

for value,index in n_list:
    if max_value <= value:
        max_value, max_index = value, index

print(max_value)
print(max_index)

## 라이브러리 사용시
n_list = []

for i in range(9):
    n = int(input())
    n_list.append(n)

print(max(n_list))
print(n_list.index(max(n_list))+1)

