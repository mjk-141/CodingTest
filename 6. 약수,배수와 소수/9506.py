while True:
    n = int(input())
    sum = 0
    n_list = []

    if n == -1:
        break

    for i in range(1, n+1):
        if n % i == 0 and i != n:
            n_list.append(i)
            sum += i
    if sum != n:
        print(f'{n} is NOT perfect.')
    else:
        print(n," = "," + ".join(str(i) for i in n_list), sep = "")