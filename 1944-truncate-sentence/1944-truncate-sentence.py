class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # split the string with the delimiter of blank space
        # slice the str
        return " ".join(s.split(" ")[:k])