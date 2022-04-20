from pool import *
from user import *

def main():
    print("Welcome to Uniswap!")

    pool1 = Pool("A", 40.0, "B", 60.0)
    pool2 = Pool("C", 80, "D", 40)

    pool1.printPool()
    



    #lp = LPToken(40.0, 60.0, .66, 1.5)
    #print(lp.liquidity)

main()