# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = [] 
        j = 0
        for i in range(len(pairs)): 
            if(i == 0):
                output.append([Pair(p.key, p.value) for p in pairs])  # Append a copy of the current state
            else: 
                j = i
                while(j > 0):
                    if(pairs[j].key < pairs[j-1].key):
                        pairs[j], pairs[j-1] = pairs[j-1], pairs[j] 
                    j-=1 
                output.append([Pair(p.key, p.value) for p in pairs])  # Append a copy of the current state
        return output
