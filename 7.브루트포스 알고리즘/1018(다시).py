m, n = map(int, input().split())
chess_board = []
for i in range(m):
    chess_board.append(list(input()))

result = []
for x in range(m-7):
    for y in range(n-7):
        cnt = 0
        for i in range(x,x+7):
            for j in range(y,y+7):
                if chess_board[i][j] == chess_board[i][j+1]:
                    if chess_board[i][j] == 'B':
                        chess_board[i][j+1] = 'W'
                    else:
                        chess_board[i][j+1] = 'B'
                    cnt += 1
                if chess_board[i][j] == chess_board[i+1][j]:
                    if chess_board[i][j] == 'B':
                        chess_board[i+1][j] = 'W'
                    else:
                        chess_board[i+1][j] = 'B'
                    cnt += 1
        result.append(cnt)

print(min(result))