class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # for each array, concatenate each word and form a one word string
        first_word = "".join(word1)
        second_word = "".join(word2)

        # compare and return result 
        return first_word == second_word