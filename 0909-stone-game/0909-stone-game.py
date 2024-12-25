class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        sorted_piles=sorted(piles)
        alice=0
        bob=0

        while sorted_piles:
            alice+=sorted_piles.pop()
            bob+=sorted_piles.pop()

        if alice>bob:
            return True
        else:
            return False
        