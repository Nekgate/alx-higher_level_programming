#!usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    This print a matrix of integers to STDOUT
    """
    for i in range(len(matrix)):
        tendr_len = len(matrix[i])
        for j in range(tendr_len):
            if j != tendr_len - 1:
                endChk = ' '
            else:
                endChk = ''
            print("{:d}".format(matrix[i][j]), end=endChk)
        print("")
