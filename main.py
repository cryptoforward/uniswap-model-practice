from multiprocessing import pool
from pool import *
from user import *

def main():
    print("Welcome to Uniswap!")

    pool1 = Pool("A", 40.0, "B", 60.0)
    pool2 = Pool("C", 80.0, "D", 40.0)
    user = User(0.0,0.0,0.0,0.0, [])

    pool1.printPool()
    print("")
    print("")
    pool2.printPool()

    option = 0
    currentPool = pool1

    print("")
    option = input("Enter top for top pool, bottom for bottom pool. Include parantheses:")

    if option == "top":
        pool1.printPool()
    elif option == "bottom":
        currentPool = pool2
        pool2.printPool()

    #enter -1 to exit
    while option !=-1:
        print("Enter 1 to swap "+ currentPool.token_1 +" for " + currentPool.token_2)
        print("Enter 2 to swap "+ currentPool.token_2 + " for "+ currentPool.token_1)
        print("Enter 3 to add liquidity")
        
        option = input()
        if option == 1 :
            option = input("Enter amount of "+ currentPool.token_1+" to send:")
            if option > 0:
                currentPool.swap1for2(option)
            else: print("No negative values!")
        elif option == 2 :
            option = input("Enter amount of "+ currentPool.token_2+" to send:")
            if option > 0:
                currentPool.swap2for1(option)
            else: print("No negative values!")
        elif option == 3:
            add_1 = input("Enter amount of "+ currentPool.token_1+" to add:")
            add_2 = input("Enter amount of "+ currentPool.token_2 + " to add:")
            currentPool.addLiquidity(add_1, add_2)

        

        currentPool.printPool()

        
        

    #lp = LPToken(40.0, 60.0, .66, 1.5)
    #print(lp.liquidity)

main()