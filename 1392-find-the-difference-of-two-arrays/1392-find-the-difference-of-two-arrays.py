class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert the two nums arr into sets
        # perform diff between the two
        # convert set into list 
        # then append to the final_ans

        nums1 = set(nums1)
        nums2 = set(nums2)

        final_ans = []
        final_ans.append(list(nums1-nums2))
        final_ans.append(list(nums2-nums1))
        
        return final_ans