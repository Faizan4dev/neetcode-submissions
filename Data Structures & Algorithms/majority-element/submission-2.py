class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        maj = 0
        for i in range(len(nums)):
            if freq == 0 :
                maj = nums[i]
            if nums[i] == maj:
                freq +=1
            else:
                freq -=1
        return maj