## 와 징한놈들
## 가로 세로 100cm 짜리 도화지를 전부 배열로 만들었누 이거 완전 노가다 씹 노가다 완전 개노가다
### 답도 없는 쉨

## 2차원 배열
Drawing_paper = [[0 for _ in range(101)] for _ in range(101)]

N=int(input())
for _ in range(N):
    l,d = map(int,input().split())
    for i in range(l,l+10):
        for j in range(d,d+10):
            Drawing_paper[i][j] = 1

cnt = 0
for i in range(101):
    cnt += Drawing_paper[i].count(1)

print(cnt)