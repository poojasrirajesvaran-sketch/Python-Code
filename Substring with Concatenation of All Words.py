from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        results = []
        
        for i in range(word_len):
            left = i
            curr_counts = Counter()
            count = 0
            
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                
                if word in word_counts:
                    curr_counts[word] += 1
                    count += 1
                    
                    while curr_counts[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        curr_counts[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == num_words:
                        results.append(left)
                else:
                    curr_counts.clear()
                    count = 0
                    left = j + word_len
                    
        return results
