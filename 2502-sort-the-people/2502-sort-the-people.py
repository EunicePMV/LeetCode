class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # init dict
        # loop through the arrs, and create key-value pair

        names_heights = dict()
        for i in range(len(names)):
            names_heights[heights[i]] = names[i]
        
        sort_heights = sorted(names_heights.keys())[::-1]
        ans = []
        for h in sort_heights:
            ans.append(names_heights[h])
        return ans

        