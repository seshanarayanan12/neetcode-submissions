class Solution:

    def encode(self, strs: List[str]) -> str:
        print(''.join(f'{len(s)}#{s}' for s in strs))
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:

        result = []

        i = 0
        while i < len(s):

            j = s.find('#', i)
            print(s[i:j])
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i+length])
            
            i += length
        
        return result

