class Pool:
    token_A = "A"
    token_B = "B"
    
    quantity_A = 40.0
    quantity_B = 60.0

    def __init__(self, name_a, quantity_a, name_b, quantity_b ):
        self.token_A = name_a
        self.token_B = name_b
        self.quantity_A = quantity_a
        self.quantity_B = quantity_b
    
    
    #Current price of A in terms of B
    def get_priceA(self):
        return self.quantity_B / self.quantity_A

    #Current price of B in terms of A
    def get_priceB(self):
        return self.quantity_A / self.quantity_B

        


class LPToken:
    range_A = [0.0, 100.0]
    range_B = [0.0, 100.0]
    #for simplicity, 1 unit of LP 
    quantity = 1.0