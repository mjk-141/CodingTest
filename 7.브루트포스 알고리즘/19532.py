## 반복문을 사용한 경우
a, b, c, d, e, f = map(int, input().split())
n_list = []
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x+b*y == c and d*x+e*y == f:
            n_list.append((x,y))

print(n_list[0][0],n_list[0][1])

## 근의 공식 사용하기
a, b, c, d, e, f = map(int, input().split())
x = 