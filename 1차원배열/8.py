## 리스트로 풀 경우
remainders = []

for i in range(10):
    n = int(input())
    if n%42 not in remainders:
        remainders.append(n%42)

print(len(remainders))


## Set 으로 푼 경우
# 나머지를 저장할 집합
remainders = {int(input()) % 42 for _ in range(10)}

# 서로 다른 나머지 개수 출력
print(len(remainders))