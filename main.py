from pool import *
from user import *

def main():
    print("Welcome to Uniswap!")

    testPool = Pool("A", 40.0, "B", 60.0)
    print(testPool.get_priceA())
    print(testPool.get_priceB()) 

    testPool.swap1for2(10)

    print(testPool.get_priceA())
    print(testPool.get_priceB()) 



    #lp = LPToken(40.0, 60.0, .66, 1.5)
    #print(lp.liquidity)

main()