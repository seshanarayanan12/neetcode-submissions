class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictR ={}
        for a in nums:
            if a in dictR:
                dictR[a] += 1
            else:
                dictR[a] = 1
        print(dictR)
        # method 1 
        # sorted_items = sorted(dictR.items(), key = lambda kv:(kv[0], kv[1]))
        # print(sorted_items)
        # finalResult = []
        # while len(finalResult) < k :
        #     finalResult.append(sorted_items.pop()[0])
        # method 2
        arr =[]
        for i, cnt in dictR.items():
            arr.append([cnt,i])
        arr.sort()
        print(arr)
        finalResult = []
        while len(finalResult) < k :
            finalResult.append(arr.pop()[1])
        print(finalResult)
        return finalResult