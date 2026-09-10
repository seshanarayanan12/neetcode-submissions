class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = {}

        # Use sorted string as Key in dict and store all the anagrams for that sorted string

        for a in strs:
            b = ''.join(sorted(a))

            #Check if b exists in resultDict, then add else create

            if b in resultDict :
                resultDict[b].append(a)
            else:
                resultDict[b] = [a]
        
        #Create a final List outof the Values of resultDict
        finalResult = list(resultDict.values())
        return finalResult