## 라이브러리 안쓰고 진행
n,m=map(int,input().split())

n_list = [i+1 for i in range(n)]

for _ in range(m):
    i,j = map(int,input().split())
    n_list[i-1:j] = n_list[i-1:j][::-1]
    
for i in range(n):
    print(n_list[i],end=" ")
    
## 라이브러리 사용
n,m=map(int,input().split())

n_list = [i+1 for i in range(n)]

for _ in range(m):
    i,j = map(int,input().split())
    n_list[i-1:j] = reversed(n_list[i-1:j])
    
for i in range(n):
    print(n_list[i],end=" ")
    