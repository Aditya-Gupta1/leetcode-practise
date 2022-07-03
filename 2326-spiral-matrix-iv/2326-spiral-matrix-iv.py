# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        temp = head
        table = [[0 for _ in range(n)] for _ in range(m)]
        left, right, up, down = 0, n-1, 0, m-1
        numEle = 0
        
        while True:
            
            # moving horizontally right
            # print("horizontally right")
            for idx in range(left, right+1):
                if temp != None:
                    table[up][idx] = temp.val
                    temp = temp.next
                else:
                    table[up][idx] = -1
                # print(up, idx, table[up][idx])
                numEle += 1
            
            up += 1
            if numEle >= m*n: break
            
            # moving vertically down
            # print("vertically down")
            for idx in range(up, down+1):
                if temp != None:
                    table[idx][right] = temp.val
                    temp = temp.next
                else:
                    table[idx][right] = -1
                # print(idx, right, table[idx][right])
                numEle += 1
            
            right -= 1
            if numEle >= m*n: break
            
            # moving horizantally left
            # print("horizontally left")
            for idx in range(right, left-1, -1):
                if temp != None:
                    table[down][idx] = temp.val
                    temp = temp.next
                else:
                    table[down][idx] = -1
                # print(down, idx, table[down][idx])
                numEle += 1
            
            down -= 1
            if numEle >= m*n: break
            
            # moving vertically up
            # print("vertically up")
            for idx in range(down, up-1, -1):
                if temp != None:
                    table[idx][left] = temp.val
                    temp = temp.next
                else:
                    table[idx][left] = -1
                # print(idx, left, table[idx][left])
                numEle += 1
            
            left += 1
            if numEle >= m*n: break
            
        return table