matrix = [[1, 2], [3, 4], [5, 6]]
i = 0
while i < len(matrix): 
    j = 0
    while j < len(matrix[i]):  
        print(matrix[i][j], end=" ")
        j += 1
    print()
    i += 1
