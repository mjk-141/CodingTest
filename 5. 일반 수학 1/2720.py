## Quater = 0.25(25), Dime = 0.10(10), Nickel = 0.05(5), Penny = 0.01(1)
Change = [25,10,5,1] ## 거스름돈 리스트

T = int(input())
result = [[0 for _ in range(4)] for _ in range(T)]

for i in range(T):
    C = int(input())
    for j in range(4):
        result[i][j]=int(C/Change[j])
        C%=Change[j]
        
for i in range(T):
    for j in range(4):
        print(result[i][j], end=" ")
    print("")