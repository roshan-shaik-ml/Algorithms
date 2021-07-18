# Author : Shaik Faizan Roshan Ali
# Date: 18th July 2021
# Email: alsahercoder@gmail.com
# About: This is the best matrix multiplication algorithm with divide and conquer strategy

'''
How this algorithm works:
    
    Given two matrices matrix1 and matrix2
    split matrix1 to 4 - n/2 matrices : a, b, c, d
    split matrix2 to 4 = n/2 matrices : e, f, g, h

    recursively pass the below 7 combinations of n/2 matrices
    p1 = strassen(a, f - h) 
    p2 = strassen(a + b, h)       
    p3 = strassen(c + d, e)       
    p4 = strassen(d, g - e)       
    p5 = strassen(a + d, e + h)       
    p6 = strassen(b - d, g + h) 
    p7 = strassen(a - c, e + f) 

    Computing the values of the 4 quadrants of the final matrix 
    c11 = p5 + p4 - p2 + p6 
    c12 = p1 + p2          
    c21 = p3 + p4           
    c22 = p1 + p5 - p3 - p7 
    
    Join the 4 quadrants
    result = [[c11, c12], [c21, c22]]
    return result matrix
'''
import numpy as np

def splitMatrix(matrix):

    dimension = len(matrix)
    matrix1 = matrix[:dimension//2, :dimension//2]
    matrix2 = matrix[:dimension//2, dimension//2:]
    matrix3 = matrix[dimension//2 : , :dimension//2]
    matrix4 = matrix[dimension//2: , dimension//2:]

    return matrix1, matrix2, matrix3, matrix4

def strassen(matrix1, matrix2):


    if len(matrix1) == 1:

        return matrix1 * matrix2
    else:
        a, b, c, d = splitMatrix(matrix1)
        e, f, g, h = splitMatrix(matrix2)
        p = strassen(a,  f - h) 
        q = strassen(a + b, h)       
        r = strassen(c + d, e)       
        s = strassen(d, g - e)       
        t = strassen(a + d, e + h)       
        u = strassen(b - d, g + h) 
        v = strassen(a - c, e + f) 

        c11 = t + s - q + u
        c12 = p + q         
        c21 = r + s          
        c22 = p + t - r - v
        result = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

        return result

if __name__ == "__main__":
  
    # driver code
    arr1 = np.array([[1,2],
                    [2, 3]])
    arr2 = np.array([[11, 22],
                    [33, 34]])
    result = strassen(arr1, arr2)
    print(result)
