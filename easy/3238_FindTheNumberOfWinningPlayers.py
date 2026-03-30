# https://leetcode.com/problems/find-the-number-of-winning-players/description/
# You are given an integer n representing the number of players in a game and a 2D array pick where pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.

# Player i wins the game if they pick strictly more than i balls of the same color. In other words,

# Player 0 wins if they pick any ball.
# Player 1 wins if they pick at least two balls of the same color.
# ...
# Player i wins if they pick at least i + 1 balls of the same color.
# Return the number of players who win the game.

# Note that multiple players can win the game.


# Example 1:
# Input: n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
# Output: 2
# Explanation:
# Player 0 and player 1 win the game, while players 2 and 3 do not win.

# Example 2:
# Input: n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]
# Output: 0
# Explanation:
# No player wins the game.

# Example 3:
# Input: n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]
# Output: 1
# Explanation:
# Player 2 wins the game by picking 3 balls with color 4.

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        records = [{0: 0} for _ in range(n)]
        currentPlayer = pick[0][0]
        for picked in pick:
            x,y = picked
            if x!= currentPlayer:
                currentPlayer = x
            records[currentPlayer][y] = records[currentPlayer].get(y,0)+1
        
        winner = 0
        for i in range(n):
            for key in records[i].keys():
                if records[i][key] > i:
                    winner +=1
                    break

        return winner 

# Time Complexity: Θ(n+m)


# Space Complexity: 
# records is a list of n dictionaries. Θ(n+m)


