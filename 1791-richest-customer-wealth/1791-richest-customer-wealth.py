class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest_customer =  0
        for account in accounts:
            richest_customer = sum(account) if sum(account) > richest_customer else richest_customer
        return richest_customer