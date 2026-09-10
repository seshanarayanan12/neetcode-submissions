class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #this solution will make use of the count of letters

        #Create a Hmap where each key is a 26-length Tuple Representing character frequencies
        res = defaultdict(list) #
        
        # Initialise a count array of size 26 with all zeroes, for each c in s, increment the count at the corresponding index

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)- ord('a')] += 1
            #convert count array to tuple
            res[tuple(count)].append(s)
        
        return  list(res.values())