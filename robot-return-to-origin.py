class Solution: #the most intuitive solution
    def judgeCircle(self, moves: str) -> bool:
        right = left = up = down = 0
        for i in moves:
            if i == 'R': 
                right += 1
            elif i == 'L':
                left +=1
            elif i == 'U':
                up += 1
            elif i == 'D':
                down += 1
        if up == down and right == left: 
            return True
        else:
            return False

class Solution(object): #leetcode solution
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1
        return x == y == 0 #came back to the origin


class Solution: #fastest solution (and easiest) with count()
    def judgeCircle(self, moves: str) -> bool:
        return (moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R'))