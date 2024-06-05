class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # initialize the arr output 
        arr = []

        # declare first element in arr element
        arr.append(first)

        # for n in encoded 
        for i in range(len(encoded)):
            arr.append(encoded[i] ^ arr[i])
        return arr