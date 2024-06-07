class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # check the prev dest if the same continue, else return 
        from_destination = set()
        for destination in paths:
            from_destination.add(destination[0])

        to_destination = set()
        for destination in paths:
            to_destination.add(destination[1])

        for city in to_destination:
            if city not in from_destination:
                return city