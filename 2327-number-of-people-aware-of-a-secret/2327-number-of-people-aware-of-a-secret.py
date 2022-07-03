class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        status = [0 for _ in range(n)]
        status[0] = 1
        itr = 0
        
        while itr < n:
            
            if status[itr] != 0:
                
                share = itr+delay
                while share < n and share < itr+forget:
                    status[share] += status[itr]
                    status[share] = status[share] % 1000000007
                    share += 1
                
                if itr+forget < n: status[itr] = 0
            
            itr += 1
        # print(status)
        total = 0
        for people in status:
            total += people
            total %= 1000000007
        
        return total
                    