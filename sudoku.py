sudoku = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 1, 5, 6, 4, 8, 9, 7],
        [5, 6, 4, 8, 9, 7, 2, 3, 1],
        [8, 9, 7, 2, 3, 1, 5, 6, 4],
        [3, 1, 2, 6, 4, 5, 9, 7, 8],
        [6, 4, 5, 9, 7, 8, 3, 1, 2],
        [9, 7, 8, 3, 1, 2, 6, 4, 5]
        ]

a =[[4, 8, 9, 3, 1, 5, 2, 6, 7],
    [1, 6, 2, 4, 9, 7, 3, 5, 8],
    [3, 5, 7, 2, 8, 6, 9, 1, 4],
    [8, 9, 5, 6, 3, 1, 4, 7, 2],
    [6, 2, 1, 7, 4, 8, 5, 9, 3],
    [7, 8, 3, 5, 2, 9, 1, 8, 6],
    [9, 1, 4, 8, 7, 3, 6, 2, 5],
    [2, 7, 6, 1, 5, 4, 8, 3, 9],
    [5, 3, 8, 9, 6, 2, 7, 4, 1]]
def tarkista(arr):
        summa = 45
        for i in arr:
                if summa != sum(i):
                        print(i)
                        return False
        for i in range(9):
                tul = 0
                for j in arr:
                       tul += j[i]
                if tul != summa:
                        print(i)
                        return False
        for k in range(3):
                for l in range(3):
                        tul = 0
                        for i in range(3):
                                for j in range(3):
                                        tul += arr[i+3*k][j+3*l]
                        if tul != summa:
                                print(k,l)
                                return False
        return True

def getGrid():
        arr = [[0 for i in range(9)]for i in range(9)]
        for i in range(9):
                for j in range(9):
                        arr[i][j] = int(input())
        return arr
#a = getGrid()
print(a)
print(tarkista(a))
print(tarkista(sudoku))
