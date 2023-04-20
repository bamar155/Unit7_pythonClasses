class Smoothie:
        def __init__(self, ingredientA,
    ingredientB, ingredientC):
                self.ingredientA=ingredientA
                self.ingredientB=ingredientB
                self.ingredientC=ingredientC 
order = Smoothie ("Almond milk,Mango,Banana")

print(order.ingredientA) 
print(order.ingredientB)
print(order.ingredientC)