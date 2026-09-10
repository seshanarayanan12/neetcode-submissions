class Solution:
    def isValid(self, s: str) -> bool:
        resultStack = []
        n = len(s)
        bracketHash = {']':'[', '}':'{', ')':'('}
        i=0
        if n==0 or n==1:
            return False
        if s[0] in bracketHash.keys():
            return False
        else:
            while i < n:
                if s[i] in bracketHash.values():
                    resultStack.append(s[i])
                    print(resultStack)
                else:
                    if resultStack and resultStack[-1] == bracketHash[s[i]]:
                        resultStack.pop()
                    else:
                        return False
                i+=1
            print(resultStack)
            if resultStack:
                return False
            else:
                return True
