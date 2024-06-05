class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        total_emp = 0 
        for hour in hours:
            if hour >= target:
                total_emp += 1
        return total_emp