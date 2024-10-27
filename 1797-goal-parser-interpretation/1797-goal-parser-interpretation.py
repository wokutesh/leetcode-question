class Solution:
    def interpret(self, command: str) -> str:
        res=command.replace('()','o')
        res1=res.replace('(al)','al')
        
        return res1
        