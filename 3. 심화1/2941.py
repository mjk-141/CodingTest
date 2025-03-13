# 크로아티아 알파벳 리스트
Croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

cnt = 0
str = input()

for word in Croatia_alphabet:
    cnt += str.count(word)

print(len(str)-(cnt*2)+cnt)
