message = []
max_len = 0
for i in range(5):
    message.append(input())
    max_len = max(max_len,len(message[i]))

## 세로 읽기
for i in range(max_len):
    for j in range(5):
        if i >= len(message[j]):
            pass
        else:
            print(message[j][i],end="")
