## 2차원 배열 채우기
Matrix= []
for i in range(9):
    Matrix.append(list(map(int,input().split())))

max_value = Matrix[0][0]
max_row = 0
max_ind = 0
for i in range(9):
    for j in range(9):
        max_value = max(Matrix[i][j],max_value)
        if max_value == Matrix[i][j]:
            max_row,max_ind = i+1,j+1
            
print(max_value)
print(max_row, max_ind)