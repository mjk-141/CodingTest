num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int,input().split())
str = ''
while N > 0:
    str += num_list[N%B]
    N //=B

print(str[::-1])