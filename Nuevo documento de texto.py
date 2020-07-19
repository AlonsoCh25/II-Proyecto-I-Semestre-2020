
list_init = []
ro = 9
col = 5

csv_scoreboard = csv_class("ScoreBoard.csv","rt")
matrix = csv_scoreboard.get_matrix()

for line in matrix:
    if line != "[" and line != "]" and line != "," and line != "[]" and line != " ":
        list_init += [int(line)]

gridMatrix = [list_init[col*i : col*(i+1)] for i in range(ro)]

print(len(gridMatrix))
print(gridMatrix)



list_init = []
#Load the list of matrix
for line in matrix[row_M][3]:
    if line != "[" and line != "]" and line != "," and line != "[]" and line != " ":
        list_init += [int(line)]

#Set matrix
gridMatrix = [list_init[5*i : 5*(i+1)] for i in range(9)]
print(gridMatrix)
