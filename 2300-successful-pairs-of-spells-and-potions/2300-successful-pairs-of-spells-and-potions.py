class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        
        for i in range(len(spells)):
            l = 0
            h = len(potions)
            n = success / spells[i]
            while l < h:
                mid = l + (h - l)//2
                if potions[mid] >= n:
                    h = mid
                else:
                    l = mid+1
            pairs.append(len(potions)-l)
        
        return pairs