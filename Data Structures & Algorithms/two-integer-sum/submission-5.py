class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        n = len(nums)
        for i in range(n):
            needed = target - nums[i]
            if needed not in need:
                need[nums[i]] = i
            else:
                return [need[needed] , i]