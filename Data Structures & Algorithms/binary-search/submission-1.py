class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        mid = 0

        while left <= right:
            mid = (left + right) // 2

            if target>nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target ==nums[mid]:
                return mid
        return -1