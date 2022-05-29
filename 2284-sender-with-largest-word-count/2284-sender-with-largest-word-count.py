class Solution:
    
    def countWords(self, message):
        return len(message.split(" "))
    
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        words = dict()
        n = len(messages)
        maxWords = 0
        sender = ""
        
        for i in range(n):
            words[senders[i]] = words.get(senders[i], 0) + self.countWords(messages[i])
            if (words[senders[i]] > maxWords) or (words[senders[i]] == maxWords and senders[i] > sender):
                maxWords = words[senders[i]]
                sender = senders[i]
        
        return sender