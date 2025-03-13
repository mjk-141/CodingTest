N = int(input())
cnt = 0
for i in range(N):
    str = input()
    str_list = list(set(str))
    deciding_factor = 0
    for i in range(len(str_list)):
        if str.count(str_list[i]) > 1:
            tmp = str.count(str_list[i])
            if str[str.index(str_list[i])] != str[str.index(str_list[i])+tmp-1]:
                deciding_factor = -1
    if deciding_factor != -1:
        cnt += 1
print(cnt)

## 
N = int(input())  # 단어 개수 입력
cnt = 0  # 그룹 단어 개수 카운트

for _ in range(N):
    word = input()  # 단어 입력
    seen = set()  # 이미 확인한 문자 저장
    prev = ''  # 이전 문자 저장
    is_group_word = True  # 그룹 단어 여부 판별

    for char in word:
        if char in seen and char != prev:
            is_group_word = False
            break
        seen.add(char)
        prev = char
    
    if is_group_word:
        cnt += 1

print(cnt)  # 그룹 단어 개수 출력

## 
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)