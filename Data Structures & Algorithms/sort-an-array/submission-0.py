class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums):
            if len(nums) <=1:
                return nums

            mid = len(nums) //2
            left_arr = nums[:mid]
            right_arr = nums[mid:]
            left_arr = mergeSort(left_arr)
            right_arr = mergeSort(right_arr)
            return merge(left_arr , right_arr)

        def merge(left_arr , right_arr):
            result = []
            i,j = 0,0
            m = len(left_arr)
            n = len(right_arr)
            while i<m and j<n:
                if left_arr[i] <= right_arr[j]:
                    result.append(left_arr[i])
                    i+=1
                else:
                    result.append(right_arr[j]) 
                    j+=1
            
            if i<m:
                while i<m:
                    result.append(left_arr[i])
                    i+=1
            if j<n:
                while j<n:
                    result.append(right_arr[j])
                    j+=1
            return result
        return mergeSort(nums)

        



