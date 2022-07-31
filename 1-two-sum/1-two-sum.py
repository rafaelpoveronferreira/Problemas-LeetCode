class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, num1 in enumerate(nums):
            for i2, num2 in enumerate(nums[:-i1]):
                if num2 + nums[i2+i1] == target:
                    return [i2, (i2+i1)]
        return 'No solution found.'
            
    