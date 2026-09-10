class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aList = {} # Tuple to store sorted strings as key and the original anagrams as values

        for i in strs:

            j = "".join(sorted(i))
            if j in aList:
                aList[j].append(i)
            else:
                aList[j] = [i]
        
        finalResult = list(aList.values())
        return finalResult