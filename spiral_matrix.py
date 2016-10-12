import math
matrix = [[1],[5],[9]]
spiral = []
last_index = len(matrix)-1
it = (min(len(matrix),len(matrix[0])) +1)/2
for i in range(it):
	spiral.extend(matrix[i][i:len(matrix[i])-i])
	for row in range(i+1,last_index-i+1):
		spiral.append(matrix[row][len(matrix[i])-1-i])
	if i != last_index-i:
		tmp = matrix[last_index-i][i:len(matrix[i])-1-i]
		spiral.extend(tmp[::-1])
	if i != len(matrix[i])-1-i:
		for row in range(last_index-i-1, i,-1):
			spiral.append(matrix[row][i])

return spiral		