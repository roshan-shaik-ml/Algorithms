# Author: Roshan Shaik
# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1


# ---------- Test Cases ----------
if __name__ == "__main__":
    sol = Solution()

    # Standard rotated array
    print(sol.search([4,5,6,7,0,1,2], 0))   # Expected 4
    print(sol.search([4,5,6,7,0,1,2], 3))   # Expected -1

    # Not rotated (normal sorted)
    print(sol.search([1,2,3,4,5,6,7], 5))   # Expected 4

    # Small array
    print(sol.search([1], 0))               # Expected -1
    print(sol.search([1], 1))               # Expected 0

    # Two elements rotated
    print(sol.search([3,1], 1))             # Expected 1
    print(sol.search([3,1], 3))             # Expected 0

    # Rotated with duplicate-like positions (no actual duplicates)
    print(sol.search([6,7,1,2,3,4,5], 2))   # Expected 3
