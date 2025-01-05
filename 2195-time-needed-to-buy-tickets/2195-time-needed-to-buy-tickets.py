class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        i = 0
        while tickets:
            
            if i >= len(tickets):
                i = 0

            if tickets[i] > 0:
                tickets[i] -= 1
                count += 1

            
            if i == k and tickets[k] == 0:
                return count

           
            if tickets[i] == 0:
                del tickets[i]
                if i < k: 
                    k -= 1

            else:
                i += 1

        return count

