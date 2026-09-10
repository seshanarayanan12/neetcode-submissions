class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffixProduct = [0] * n
        prefixProduct = [0] * n
        finalProduct = [0] * n
        # Calculate prefix product
        prefixProduct[0] = suffixProduct[n-1] = 1
        for i in range(1,n):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
        print(prefixProduct)
        for i in range (n-2, -1, -1):
            suffixProduct[i] = nums[i+1] * suffixProduct[i+1]
        print(suffixProduct)
        for i in range (n):
            finalProduct[i] = prefixProduct[i] * suffixProduct[i]
        return finalProduct