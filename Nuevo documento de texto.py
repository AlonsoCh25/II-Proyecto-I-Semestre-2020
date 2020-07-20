from CLASSES import *
def sort_matrix():
    sort = True
    archive_csv = csv_class("ScoreBoard.csv","rt")
    matrix_csv = archive_csv.get_matrix()
    row = 0
    minutes = 7
    seconds = 8
    while sort:
        if len(matrix_csv)-1 > row:
            if matrix_csv[row][minutes] < (matrix_csv[row+1][minutes]):
                B = matrix_csv[row][minutes]
                matrix_csv[row][minutes] = matrix_csv[row+1][minutes]
                matrix_csv[row+1][minutes] = B
                row = 0
            elif matrix_csv[row][minutes] == matrix_csv[row+1][minutes]:
                if matrix_csv[row][seconds] < matrix_csv[row+1][seconds]:
                    B = matrix_csv[row][seconds]
                    matrix_csv[row][seconds] = matrix_csv[row+1][seconds]
                    matrix_csv[row+1][seconds] = B
                    row = 0
                elif matrix_csv[row][minutes] >= matrix_csv[row+1][minutes]:
                    row += 1
            elif matrix_csv[row][minutes] > matrix_csv[row+1][minutes]:
                row += 1
        else:
            archive_csv.write(matrix_csv)
            archive_csv.update_matrix("ScoreBoard.csv","w")
            sort = False
