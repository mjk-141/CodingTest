n = int(input())
n_list = []
for i in range(1,n+1):
    num = i + sum(map(int,str(i)))
    if num == n:
        n_list.append(i)

if n_list:
    print(n_list[0])
else:
    print(0)