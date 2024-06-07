class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # loop through the items
        # check what type of ruleKey
            # 1. declare a dict with key the index, and the value the type, color, or name
        # check if the ruleValue in list 
        # if yes: add 1 else continue
        typeValue = {"type": 0, "color": 1, "name": 2}
        index = typeValue[ruleKey]

        matched = 0
        for item in items:
            if ruleValue == item[index]:
                matched += 1
        return matched