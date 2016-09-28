matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print matrix
it = len(matrix)/2
last_index = len(matrix)-1
for row in range(it):
    tmp_range = range(row, last_index-row)
    for column in tmp_range:
        tmp = matrix[row][column]
        matrix[row][column] = matrix[last_index-column][row]
        matrix[last_index-column][row] = matrix[last_index-row][last_index-column]
        matrix[last_index-row][last_index-column] = matrix[column][last_index-row]
        matrix[column][last_index-row] = tmp
    
print matrix