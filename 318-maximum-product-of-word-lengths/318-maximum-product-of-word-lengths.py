class Solution:
    def compare(self, word1, word2):
        # approach 1
        words = set(list(word1))
        for ch in word2:
            if ch in words: return False
        return True
    
    def maxProduct(self, words: List[str]) -> int:
        # approach 1
        n = len(words)
        maxProduct = 0
        
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if self.compare(words[i], words[j]):
        #             maxProduct = max(maxProduct, len(words[i])*len(words[j]))
        # return maxProduct
        
        # approach 2
        char_set = [set(word) for word in words]
        for i in range(n):
            for j in range(i+1, n):
                if not char_set[i] & char_set[j]:
                    maxProduct = max(maxProduct, len(words[i])*len(words[j]))
        return maxProduct