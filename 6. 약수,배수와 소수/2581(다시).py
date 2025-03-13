M = int(input())
N = int(input())
n_list = []
for i in range(M, N+1):
    decision = 0
    for j in range(2, i):
        if i % j == 0:
            decision = 0
            break
        else:  # 소수라는것을 의미
            decision = 1
    if decision == 1:
        n_list.append(i)

if len(n_list) > 0:
    print(sum(n_list))
    print(n_list[0])
else:
    print(-1)
