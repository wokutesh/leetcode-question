class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda item:(-item[0],item[1]))
        ans=[]
        for p in people:
            ans.insert(p[1],p)

        return ans

        