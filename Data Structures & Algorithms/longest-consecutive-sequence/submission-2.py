class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcsSet=set(nums)
        longest = 0
        
        # [0,1,1,2,3,4,5,6] ==> [0,1,2,3,4,5,6] ==> 7
        for num in lcsSet:
            # CHeck if this is the start of the sequence
            if (num-1) not in lcsSet:
                length = 1 # initialise the length
                # Now to see if there is a sequence from the start
                # for each of the number  + length to check seq in the Set
                while (num+length) in lcsSet:
                    length += 1 
                longest = max(length,longest)
        return longest
            