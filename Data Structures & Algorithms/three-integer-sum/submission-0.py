class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        finalResult = []
        for i in range(len(nums)- 1):
            if nums [i] == nums[i-1] and i>0:
                continue
            j = i + 1
            k = len(nums)-1
            
            while j < k :
                targetSum = nums[i] + nums[j] + nums[k]
                if targetSum > 0 :
                    k -= 1
                elif targetSum < 0:
                    j += 1
                else:
                    finalResult.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1 
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return finalResult