from math import *
import array as arr
from user import *

class Pool:
    def __init__(self, name_a, quantity_a, name_b, quantity_b ):
        self.token_1 = name_a
        self.token_2 = name_b
        self.quantity_1 = quantity_a
        self.quantity_2 = quantity_b

    #Current price of A in terms of B
    def get_priceA(self):
        return self.quantity_2 / self.quantity_1

    #Current price of B in terms of A
    def get_priceB(self):
        return self.quantity_1 / self.quantity_2

    def get_liquidity(self):
        return sqrt(self.quantity_1*self.quantity_2)

    #returns quantity of token 2 received
    def swap1for2(self, quantity_given  ):
        k = self.quantity_1 * self.quantity_2
        self.quantity_1 += quantity_given
        received = ((self.quantity_1*self.quantity_2)-k)/ self.quantity_1
        self.quantity_2 -= received
        return received

    # Same as previous but switched
    def swap2for1(self, quantity_given):
        k = self.quantity_1* self.quantity_2
        self.quantity_2+= quantity_given
        received = ((self.quantity_2*self.quantity_1)-k)/ self.quantity_2
        self.quantity_2 -= received
        return received

    def printPool(self):
        #print(self.token_1+"      " +self.token_2)
        print(self.token_1+"      __  "+self.token_2)
        print("      (__) ")
        print(" {a}  __ {b}     ".format(a=self.quantity_1, b=self.quantity_2))
        print("      (__) ")
    




    

    

    

        

# lower/upper ratio are for concentrated liquidity feature
# ratio inputs should be in terms of price of A (quantity B/ quantity A)
class LPToken:
    def __init__(self, quantity_1, quantity_2, lowerRatio, upperRatio):
        self.liquidity = sqrt(quantity_1*quantity_2)
        self.lower = lowerRatio
        self.upper = upperRatio

    
    