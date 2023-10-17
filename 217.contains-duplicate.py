# EASY

# first submission
# runtime: 527 ms O(n log n)
# memory: 28.4 MB   
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n = len(nums)
        if n < 2:
            return False
            
        idx = 1
        while idx != n:
            if nums[idx] == nums[idx - 1]:
                return True
            
            idx += 1

        return False
    
    
# second submission
# runtime: 464 ms O(n)
# memory: 30.88 MB   
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)