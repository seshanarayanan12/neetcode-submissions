class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countA = Counter(s)
        countB = Counter(t)
        
        if countA == countB:
            result = True
        else:
            result = False
        
        return result