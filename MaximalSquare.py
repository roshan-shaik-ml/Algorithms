"""
  LeetCode 221: Maximal Square (Using memoization)
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        # Fill the memo matrix with the following rules
        """
        - Go through each cell in the matrix
        - If the cell value is '1', 
        - Assume it as the bottom_right corner of a square
        - Check its top_right, botom_left, and top_left cells
        - Take the minimum of those three and add 1, 
        - That gives the size of the square ending at this cell
        - Parallelly, track of the largest square found
        """

        max_side_length = 0
        for i in range(0, len(memo)):

            for j in range(0, len(memo[0])):

                if matrix[i][j] == "1":

                    if i == 0 or j == 0:
                        # 0th row 
                        memo[i][j]= 1
                    else:
                        bottom_left = memo[i][j-1]
                        top_right = memo[i-1][j]
                        top_left = memo[i-1][j-1]
                        memo[i][j] = min([bottom_left, top_right, top_left]) + 1
                    
                    max_side_length = max(max_side_length, memo[i][j])
                    
        return max_side_length ** 2 
        
if __name__ == "__main__":
    
    solution = Solution()
    
    matrix_1 = [["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]]
                
    matrix_2 = [["0","1"],["1","0"]]
    
    matrix_3 = [["0"]]
    
    assert solution.maximalSquare(matrix_1) == 4
    assert solution.maximalSquare(matrix_2) == 1
    assert solution.maximalSquare(matrix_3) == 0
