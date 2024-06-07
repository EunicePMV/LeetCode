class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # isolate from_city and to_city
        to_city = set()
        from_city = set()
        for path in paths:
            to_city.add(path[1])
            from_city.add(path[0])
        return (to_city - from_city).pop()

        # check each city in to_city if in from_city, if not return

