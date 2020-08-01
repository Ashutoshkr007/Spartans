def inboard(board, word, i, j, index):
    print('i = ', i,'j =', j,'index =', index)
    if index == len(word):
        return 1

    if i < 0 or j < 0 or i > len(board) or j > len(board[0]):
        return 0

    try:
        if word[index] != board[i][j]:
            return 0
    except Exception:
        return 0

    temp = board[i][j]
    board[i][j] = ' '

    if inboard(board, word, i + 1, j, index+1):
        return 1
    elif inboard(board, word, i - 1, j, index+1):
        return 1
    elif inboard(board, word, i, j + 1, index+1):
        return 1
    elif inboard(board, word, i, j - 1, index+1):
        return 1

    board[i][j] = temp
    return 0


def search(board, word):
    for i in range(3):
        for j in range(4):
            if word[0] == board[i][j] and inboard(board, word, i, j, 0):
                return 1
    return 0


board = []
for _ in range(3):
    board.append(input().split())

print(board)
word = input("Enter The word to be searched")
if search(board, word):
    print(word, "In the given board")
else:
    print(word, "not in board")