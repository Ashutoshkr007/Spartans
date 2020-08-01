def safe(chess, total_queens, row_no, col_no):
    # coloumn
    for i in range(row_no):
        if chess[i][col_no] == 1:
            return 0
    # row
    for j in range(col_no):
        if chess[row_no][j] == 1:
            return 0
    #LR diagonal
    i, j = row_no, col_no
    while i >= 0 and j >=0:
        if chess[i][j] == 1:
            return 0
        i -= 1
        j -= 1
    #RL diagonal
    i, j = row_no, col_no
    while i >= 0 and j >= 0:
        if chess[i][j] == 1:
            return 0
        i -= 1
        j -= 1
    return 1


def queens(chess, total_queen, row_no):
    # base
    if row_no == total_queen:
        print(chess)
        return 1

    for col_no in range(total_queen):
        print(chess)
        if safe(chess, total_queen, row_no, col_no):
            chess[row_no][col_no] = 1
            next_row = queens(chess, total_queen, row_no + 1)
            if next_row:
                return 1
            chess[row_no][col_no] = 0
    return 0


n = int(input("No. of Queens"))
chess = []
for i in range(n):
    chess.append([])
    for _ in range(n):
        chess[i].append(0)
queens(chess, n, 0)