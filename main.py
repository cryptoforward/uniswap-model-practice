from pool import *

def main():
    print("Welcome to Uniswap!")

    testPool = Pool("A", 40.0, "B", 60.0)

    print(testPool.get_priceA())
    print(testPool.get_priceB()) 

main()