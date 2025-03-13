# 1차 풀이
# 10 진수 넘어가는 경우에 해당
[['A', 10], ['B', 11], ['C', 12], ['D', 13], ['E', 14], ['F', 15], ['G', 16], ['H', 17], ['I', 18], ['J', 19], ['K', 20], ['L', 21], ['M', 22], ['N', 23], ['O', 24], ['P', 25], ['Q', 26], ['R', 27], ['S', 28], ['T', 29], ['U', 30], ['V', 31], ['W', 32], ['X', 33], ['Y', 34], ['Z', 35]]
new_notation = []
for i in range(36):
    if i > 9:
        word = ord('A')+(i-10)
    else:
        word = ord('0')+i
    new_notation.append([chr(word),i])

N,B = input().split()
B=int(B)
N = N[::-1]

sum = 0
for i in range(len(N)):
    for j in range(len(new_notation)):
        if N[i] in new_notation[j]:
            sum+=new_notation[j][1]*(B**i)
print(sum)

# 2차 풀이
num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum, cnt = 0, 0
N, B = input().split()
B = int(B)
cnt = 0
for i in range(len(N)-1, -1, -1):
    sum += (num_list.index(N[i])+1)*(B**cnt)
    cnt += 1
    print(sum)
