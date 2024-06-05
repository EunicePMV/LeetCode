class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # loop over the operations,  check every term
        # check if it has plus sign or minus sign
        # if plus sign, add, else minus
        total = 0 
        for operation in operations:
            if '+' in operation:
                total += 1
            else:
                total -= 1

        return total


        