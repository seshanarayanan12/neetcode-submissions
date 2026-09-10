class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort algo
        # Create a dict/bucket where the index is the count of freq of elements 
        # i(count): 0  1   2   3  4  5  6
        # values  : 0 [1] [2] [3] 0  0  0

        count = {}
        freq = [ [] for i in range(len(nums) + 1)]
        
        # Count the frequency of elements occurring in nums
        for n in nums:
            count[n] = 1 + count.get(n,0)
        print(count)
        #Based on count as index, append the value to the frequency array(bucket)
        for n,c in count.items():
            freq[c].append(n)
        print(freq)
        res = []

        # Reverse traversal of frequency to get the most frequent elements
        for i in range (len(freq)-1,0,-1):
            # traverse each element of freq if it is a sublist
            for n in freq[i]:
                    res.append(n) # append the element in position i
                    # Setup exit condition to get the top K elements
                    if len(res) == k:
                        return res