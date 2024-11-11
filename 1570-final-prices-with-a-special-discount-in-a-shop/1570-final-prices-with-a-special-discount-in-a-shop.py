class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer=[]
        for i in range(len(prices)):
            discount=False
            for j in range(i+1,len(prices)):
                if j>i and prices[j]<=prices[i]:
                    answer.append(prices[i]-prices[j])
                    discount=True
                    break
            if not discount:

                answer.append(prices[i])
        return answer
        