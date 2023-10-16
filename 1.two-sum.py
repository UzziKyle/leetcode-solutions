# EASY

# first algorithm 
# runtime: 4941 ms O(n^2)
# memory: 17.1 MB
def twoSum(nums: list[int], target: int) -> list[int]:
    idx = range(len(nums))
    for i in idx:
        for j in idx[::-1]:
            if (nums[i] + nums[j]) == target and i != j:
                return [i, j]

# second algorithm
# runtime: 3304 ms O(n^2)
# memory: 17 MB
def two_sum(nums: list[int], target: int) -> list[int]:
    idx = range(len(nums))
    for i in idx:
        j = len(nums) - 1
        while j > i:
            print(i, j)
            if (nums[i] + nums[j]) == target and i != j:
                return [i, j]
            j -= 1
            
# third algorithm, 'learned' from the internet
# runtime: 66 ms O(n)
# memory: 17.6 MB
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, value in enumerate(nums):
            looking_for = target - nums[idx]

            if looking_for in seen:
                return [seen[looking_for], idx]

            seen[value] = idx


        return [-1, -1]