class Solution
    def twoSum(self, nums List[int], target int)
        length=len(nums)
        for i in range (length-1)
            for j in range(i+1,length)
                if nums[i]+nums[j]==target
                    return {i,j}