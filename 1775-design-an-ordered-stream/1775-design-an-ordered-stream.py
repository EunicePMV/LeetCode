class OrderedStream:

    def __init__(self, n: int):
        self.lst = ['']*n
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        # insert the value in the stream
        self.lst[idKey - 1] = value


        # STOP HERE:
        # 1. [d, e] is not printing 
        # 2. self.ptr did not match

        # return the lst that has the value of the current pointer up until to ith position with value
        temp_lst = []
        if self.ptr == idKey:
            # temp_lst = [self.lst[idKey-1]]
            temp_lst.append(self.lst[idKey-1])
            
            # For loop become false after 4
            # it exit the loop when it reached 5
            for i in range(idKey, len(self.lst)):
                self.ptr += 1
                if self.lst[i] != '':
                    temp_lst.append(self.lst[i])
                else:
                    break
                    # return temp_lst
        return temp_lst




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)