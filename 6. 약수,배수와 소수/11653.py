N = int(input())
n_list = [2]
for i in range(3, N+1):
    if N % i == 0:
        decision = 0
        for j in range(2, i):
            if i % j == 0:
                decision = 0
                break
            decision = 1
        if decision == 1:
            n_list.append(i)

result = []
cnt = 0
while True:
    if N == 1:
        break

    if N % n_list[cnt] == 0:
        result.append(n_list[cnt])
        N //= n_list[cnt]
    else:
        cnt += 1

for i in result:
    print(i)