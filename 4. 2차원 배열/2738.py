## 입력
# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100

N,M = map(int, input().split())
## 행렬 저장 리스트
Matrix_A,Matrix_B = [],[]
for i in range(2):
    if i==0:
        for _ in range(N):
            Matrix_A.append(list(map(int,input().split())))
    else:
        for _ in range(N):
            Matrix_B.append(list(map(int,input().split())))

## 행렬 합치기
for i in range(N):
    for j in range(M):
        Matrix_A[i][j]+=Matrix_B[i][j]
        print(Matrix_A[i][j],end=" ")