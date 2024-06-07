class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # initialize a list 
        # place char in its position
        # join the list of char 
        str_lst = ['']*len(s)
        for i in range(len(str_lst)):
            str_lst[indices[i]] = s[i]
        return "".join(str_lst)