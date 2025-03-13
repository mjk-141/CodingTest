n,m= map(int,input().split())

n_list = [0 for _ in range(n)]

for _ in range(m):
    i,j,k = map(int,input().split())
    
    for num in range(i-1,j):
        n_list[num] = k

for i in range(n):
    print(n_list[i],end=" ")