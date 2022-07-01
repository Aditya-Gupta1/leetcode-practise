class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        totalUnits = 0
        totalBoxes = truckSize
        idx = 0
        
        while truckSize > 0 and idx < len(boxTypes):
            numBoxes = boxTypes[idx][0] if boxTypes[idx][0] <= truckSize else truckSize
            totalUnits += numBoxes * boxTypes[idx][1]
            truckSize -= boxTypes[idx][0] if boxTypes[idx][0] <= truckSize else truckSize
            idx += 1
        
        return totalUnits
            
        