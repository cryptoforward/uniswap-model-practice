from pool import *

# User with 4 token balances, and an array of LP positions
class User:
    positions = []
    def __init__(self, a, b, c, d, LPs):
        self.balanceA = a
        self.balanceB = b
        self.balanceC = c
        self.balanceD = d
        self.positions.extend(LPs)

    
        