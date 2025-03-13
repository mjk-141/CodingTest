X = int(input())
a, b, line = 1, 1, 1

# X가 몇번째 라인인지 파악
while X > line:
    X -= line
    line += 1

# 라인이 파악 되었으면 가즈아
if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(f'{a}/{b}')
