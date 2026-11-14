def add_to_cart(item, price ,cart= None):
    if cart is None:
        cart = []
        return "cart is empty, you have not added anything to cart"
    
    cart('Dozen of spoons', 200)
    
print(add_to_cart('Dozen of spoon', 200))