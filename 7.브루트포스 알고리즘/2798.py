# 내장함수로 함 해보자
from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_num = 0
for combine in list(combinations(arr, 3)):
    if sum(combine) <= m:
        max_num = max(max_num, sum(combine))

print(max_num)