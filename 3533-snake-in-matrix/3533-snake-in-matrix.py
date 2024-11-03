class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row,col=0,0

        direction={
            'UP':(-1,0),
            'DOWN':(1,0),
            'LEFT':(0,-1),
            'RIGHT':(0,1)

        }

        for com in commands:

            dr,dc=direction[com]

            row+=dr
            col+=dc

        return row*n+col