phone_str = input()
dial_list = [("-1"),("-1"),("1"),("A,B,C"),("D,E,F"),("G,H,I"),("J,K,L"),("M,N,O"),("P,Q,R,S"),("T,U,V"),("W,X,Y,Z")]
count = 0
for str in phone_str:
    for i in range(len(dial_list)):
        for j in range(len(dial_list[i])):
            if str in dial_list[i][j]:
                count += i
                break

print(count)