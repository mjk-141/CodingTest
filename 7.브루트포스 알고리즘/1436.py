N = int(input())
n_list = []
num, cnt = 0, 0
while True:
    if '666' in str(num):
        cnt += 1
        if cnt == N:
            print(str(num))
            break
    num += 1
