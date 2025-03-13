str = input()
count = 0
for i in range(len(str)):
    if str[i] != str[len(str)-i-1]:
        count = 0
        break
    else:
        count=1
print(count)

## 다른 사람 답안
word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)
