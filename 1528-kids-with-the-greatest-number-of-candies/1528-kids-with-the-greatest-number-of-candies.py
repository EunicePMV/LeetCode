class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # keep track of the current greatest candies 
        greatest_candies = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= greatest_candies:
                result.append(True)
            else:
                result.append(False)
        return result

        