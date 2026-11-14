

VALID_COUPONS =  ["SAVE10", "WELCOME", "VIP20"]
DISCOUNT_RATE = 0.10

def is_valid_coupon(code):
    """Return True coupon code is on the list of valid code """
    return code in VALID_COUPONS

def  add_to_cart(item, price, cart=None):
    """Add  an (item, price) tuple to the cart and return the cart."""

    if cart is None:
        cart = []
    cart.append((item,price))
    return cart


def checkout(cart,coupon=None):
    """Return (final_total,status_message) for the given cart"""
    if not cart:
        return 0, "cart is empty"

    total=sum(price for _,price in cart)

    if is_valid_coupon(coupon):
        total *= 1 - DISCOUNT_RATE
        message = f"Coupon {coupon } applied: 10% off"
    elif coupon:
        message = f"Coupon {coupon} is not valid, no discount applied"
    else: 
        message = "No coupon used"

    return round(total, 1), message

def print_receipt(total,message):
    """Print the receipt."""
    print("=" * 55)
    print("RECEIPT")
    print("=" * 55)  
    print(cart1)         
    print(f"status: {message}")

    print(f"Total: Kshs.{total:.1f}")
   
    print(f"Total: Kshs.{total:.2f}")
    print("=" * 55)

if __name__ == "__main__":
    cart1= add_to_cart('Electric kettle', 950.00)
    
    
   

    
    print_receipt(*checkout(cart1, "SAVE10"))
   
    
    print("Thank you for shopping with us!")
    