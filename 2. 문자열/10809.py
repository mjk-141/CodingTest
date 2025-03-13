## 어렵게
str= list(map(str,input()))
for i in range(97,123):
    num = -1
    for j in range(0,len(str)):
        if chr(i)==str[j]:
            num = j
            break
    print(num,end=' ')

## 더 간단하게 할 수 있다.
str = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(alpha):
    print(str.find(i),end=' ')