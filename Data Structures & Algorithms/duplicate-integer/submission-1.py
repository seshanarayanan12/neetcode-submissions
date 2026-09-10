class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  count = Counter(nums)

        #  for n in nums:

        # Normal Sorted array method

        sortedArray = nums.sort()
        result = False
        for i in range(len(nums)):
            if i < len(nums)-1:
                j = i+1
                if nums[i]==nums[j]:
                    result = True
                    break
                else:
                    result = False
        return result