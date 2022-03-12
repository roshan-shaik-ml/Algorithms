'''
    Author: Shaik Faizan Roshan Ali
    Date: 12th March 2022
    Link: https://leetcode.com/problems/maximum-score-words-formed-by-letters/
'''

from collections import Counter
class Solution:
    
    def solve(self, words, freq, score, index) -> int:
        
        if index == len(words):
            return 0

        score_no = self.solve(words, freq, score, index+1) + 0
        
        word_score = 0
        consider = True
        for ch in words[index]:

            if freq[ch] == 0:
                
                consider = False 
            
            freq[ch] -= 1
            word_score += score[ord(ch)-ord('a')]
        
        score_yes = 0
        if consider == True:

            score_yes = word_score + self.solve(words, freq, score, index+1)
        
        for ch in words[index]:

            freq[ch] += 1
        
        return max(score_yes, score_no)
    
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        freq = Counter(letters)
        return self.solve(words, freq, score, 0)
