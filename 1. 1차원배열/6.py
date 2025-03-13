n,m = map(int,input().split())

n_list = list(i+1 for i in range(n))

for _ in range(m):
    i, j = map(int,input().split())
    n_list[i-1],n_list[j-1] = n_list[j-1],n_list[i-1]
    
for i in range(n):
    print(n_list[i],end=" ")