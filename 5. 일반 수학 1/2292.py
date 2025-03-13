# 둘래 넓어지는 공식
# b =   1 3 5 7 9
# a = 1 2 3 4 5 6
# h = 1
N = int(input())
sum = 1
i = 1
while N > sum:
    sum += 6*i
    i += 1
print(i)
