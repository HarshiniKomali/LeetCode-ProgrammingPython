# Problem Statement
#Title : Divisor Game
#Difficulty : Easy
#Tags: Math, Dynamic Programming
"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
"""

#Python 2 Solution
#Only the main function is included
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N%2 == 0
     
"""
Comments: Though at first this seems like a dynamic programming problem, where we need to store if Alice wins or not for different values of N,
it is a simple math problem. If N is even, Alice chooses x = 1, which makes N = N -1 i.e. odd number. 
If the new number is prime, Bob has no choice but to choose x = 1 which eventually makes Alice the winner. 
If the new number is not prime, Bob should choose x such that it is number. This makes N - x even and Alice can somehow pick x in such a way that Bob ends up with prime number and looses.
If N is even, Alice definitely wins.
If N is odd, Bob wins in any case.
"""
