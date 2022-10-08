
# Xuất ma trận
import numpy as np
def printing(quiz):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("....................")

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")

            if col == 8:
                print(quiz[row][col])
            else:
                print(str(quiz[row][col]) + " ", end="")


# Kiểm tra xem ma trận có hợp lý không
def isSafe(grid, row, col, num):
   
    # nếu tìm thấy cùng một số trong hàng tương tự, trả về false
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # nếu tìm thấy cùng một số trong cột tương tự, trả về false
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    #  nếu tìm thấy cùng một số trong ma trận 3 * 3 cụ thể, trả về false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
