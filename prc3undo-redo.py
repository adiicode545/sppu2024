# function definations


def inputMatrix():
    row = int(input("Enter no. of rows: "))
    col = int(input("Enter no. of coloumns: "))

    matrix = []
    for i in range(0, row):
        innerList = []
        for j in range(0, col):
            element = int(input("Enter element in row " +
                          str(i+1)+" and column "+str(j+1)+" : "))
            innerList.append(element)
        matrix.append(innerList)

    return matrix


def addMatrix(matrix1, matrix2):
    res = []
    # perform add operation when size of both matrix is same and no. of row in matrix 1 == no. of column in matrix 2
    if (len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[1])):
        for i in range(0, len(matrix1)):
            innerResult = []
            for j in range(0, len(matrix1[0])):
                add = matrix1[i][j] + matrix2[i][j]
                innerResult.append(add)

            res.append(innerResult)
        return res
    else:
        print("Dimensions of matrices does not match")


def substractMatrix(matrix1, matrix2):
    res = []
    # perform add operation when size of both matrix is same and no. of row in matrix 1 == no. of column in matrix 2
    if (len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[1])):
        for i in range(0, len(matrix1)):
            innerResult = []
            for j in range(0, len(matrix1[0])):
                add = matrix1[i][j] + matrix2[i][j]
                innerResult.append(add)

            res.append(innerResult)
        # return res
    else:
        print("Dimensions of matrices does not match")


def multiplyMatrix(matrix1, matrix2):
    res = []
    #  no. of row in matrix 1 == no. of column in matrix 2
    if (len(matrix1) == len(matrix2[0])):
        for i in range(len(matrix1)):  # col
            innerResult = []
            # col element of matrix 1 - row
            for j in range(len(matrix1[0])):
                mul = 0
                # col element of matrix 2 - row
                for k in range(len(matrix2[0])):
                    mul = mul + matrix1[i][k] * matrix2[k][j]
                    # print(k, " ", i, " ", j)
                    # (A[0][0] * B[0]{0})
                    # (A[0][1] * B[1]{0})

                    """ 
                        A = 2 3  -> A[0]
                            5 4  -> A[1]

                        B = 3 6
                            1 8

                        A * B = (2 * 3 + 3 * 1) (2 * 6 + 3 * 8) 
                                (5 * 3 + 4 * 1) (5 * 6 + 4 * 8)

                        Code:   (A[0][0] * B[0][0] + A[0][1] * B[1][0])   (A[0][0] * B[1][0] + A[0][1] * B[1][1])       
                                (A[1][0] * B[0][0] + A[1][1] * B[1][0])   (A[1][0] * B[1][0] + A[1][1] * B[1][1])  

                    """
                innerResult.append(mul)
            res.append(innerResult)
        return res
    else:
        print("No. of rows of 1st matrix are not equal to no. of coloumns of 2nd matrix")


# main
matrix1 = inputMatrix()
matrix2 = inputMatrix()

# operations
add = addMatrix(matrix1, matrix2)
substract = substractMatrix(matrix1, matrix2)


print("\nmatrix1 : ", matrix1)
print("\nmatrix2 : ", matrix2)
print("\nmatrix1 + matrix2  = ", add)
print("\nmatrix1 - matrix2  = ", substract)
print("\nmatrix1 * matrix2  = ", multiplyMatrix(matrix1, matrix2))

