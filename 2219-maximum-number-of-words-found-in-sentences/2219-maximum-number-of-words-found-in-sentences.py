class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # keep track of the max words
        maxWords = 0
        # loop through the 2D array 
        for sentence in sentences:
            # separate each word for each sentence 
            countWords = len(sentence.split(' '))
            maxWords = countWords if countWords > maxWords else maxWords
        return maxWords
        