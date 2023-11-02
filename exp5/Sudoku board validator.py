def validate_sudoku(board):
    import numpy as np
    board=np.array(board)
    for x in range(0,9):
        if 0 in board[x]:
            return False
    for x in range(0,9):
        dic={}
        for y in board[x]:
            if y not in dic:
                dic[y]=1
            else:
                return False
        dic2={}
        for y in board[:,x]:
            if y not in dic2:
                dic2[y]=1
            else:
                return False
    boxes= [{} for i in range(9)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3 ) * 3 + j // 3
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                if boxes[box_index][num] > 1:
                    return False
    return True