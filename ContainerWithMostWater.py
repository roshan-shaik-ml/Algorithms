from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        back, front = 0, len(height) - 1

        max_area = float('inf') * -1
        while back < front:

            area = min(height[front], height[back]) * (front - back)
            max_area = max(area, max_area)
            
            if (height[front] < height[back]):
                front -= 1
            else:
                back += 1
        
        return max_area


if __name__ == "__main__":
    
    solution = Solution()
    
    test_case_1 = [1,8,6,2,5,4,8,3,7] 
    
    assert solution.maxArea(test_case_1) == 49
    
    test_case_2 = [1,1]
    assert solution.maxArea(test_case_2) == 1
    
    test_case_3 = [1, 2, 4, 3]
    assert solution.maxArea(test_case_3) == 4
    
