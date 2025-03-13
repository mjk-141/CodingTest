## 킹 1, 퀸 1, 룩 2, 비숍 2, 나이트 2, 폰 8
chess_list = list(map(int,input().split()))

correct_list = [1,1,2,2,2,8]

for i in range(6):
    if chess_list[i] > correct_list[i]:
        print(correct_list[i]-chess_list[i], end=" ")
    elif chess_list[i] == correct_list[i]:
        print(chess_list[i]-correct_list[i], end=" ")
    else:
        print(correct_list[i]-chess_list[i], end=" ")
    
## 다른 사람 답안
chess = [1, 1, 2, 2, 2, 8]

myInput = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i] - myInput[i], end = ' ')