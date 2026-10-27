class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        count_zero = 0
        count_one = 0
        count_two = 0
        for i in range(n):
            if nums[i] == 0:
                count_zero +=1
            elif nums[i] == 1:
                count_one +=1
            else:
                count_two +=1
        # print(count_zero , count_one , count_two)
        
        for j in range(n):
            if count_zero > 0:
                nums[j] = 0
                count_zero -=1
            elif count_one > 0:
                nums[j] = 1
                count_one -=1
            else:
                nums[j] = 2
                count_two -=1