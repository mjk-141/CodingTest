# 내가한거
# p, q = map(int, input().split())
# cnt = 0
# for i in range(1, p+1):
#     if p % i == 0:
#         cnt += 1
#     if i == q and p % i == 0:
#         print(cnt)
#     if i == q and p % i != 0:
#         print(0)

# list 사용한 버전
p, q = map(int, input().split())
n_list = []
for i in range(1, p+1):
    if p % i == 0:
        n_list.append(i)

if q in n_list:
    print(n_list.index(q)+1)
else:
    print(0)