"""
Build a simple online store checkout system with three functions:

1. is_valid_coupon(code): Checks if a coupon code is in a list of valid codes (["SAVE10", "WELCOME", "VIP20"]). 
Returns True or False directly without using if/else.

2. add_to_cart(item, price, cart=None): Safely adds an (item, price) tuple to a shopping cart list without falling 
into the mutable default trap, and returns the updated cart.

3. checkout(cart, coupon=None):
	• Uses an early return if the cart is empty (returns 0, "Cart is empty").
	• Calculates the total price and applies a 10% discount if a valid coupon is given.
	• Returns multiple values: the final total and a status message.

    
	• Finally, write a helper function print_receipt(total, message) that prints the receipt and returns None by default.
    
    """
VALID_COUPONS = ["SAVE10", "WELCOME", "VIP20"]


def is_valid_coupon(code):
    """Return True if the code is a valid coupon, else False."""
    return code in VALID_COUPONS


def add_to_cart(item, price, cart=None):
    """Add an (item, price) tuple to the cart and return the cart.

    Uses None as the default to avoid the mutable default argument trap:
    a default like cart=[] would be created once and shared across calls.
    """
    if cart is None:
        cart = []
    cart.append((item, price))
    return cart


def checkout(cart, coupon=None):
    """Return (final_total, status_message) for the given cart."""
    # Early return for an empty cart
    if not cart:
        return 0, "Cart is empty"

    total = sum(price for _, price in cart)

    if coupon and is_valid_coupon(coupon):
        total *= 0.90
        message = f"Coupon '{coupon}' applied: 10% discount"
    elif coupon:
        message = f"Coupon '{coupon}' is invalid: no discount applied"
    else:
        message = "No coupon used"

    return round(total, 2), message


def print_receipt(total, message):
    """Print the receipt. Returns None implicitly (no return statement)."""
    print("=" * 30)
    print("RECEIPT")
    print("=" * 30)
    print(f"Status: {message}")
    print(f"Total:  ${total:.2f}")
    print("=" * 30)


# --- Demo ---
if __name__ == "__main__":
    # Empty cart (early return)
    total, msg = checkout([])
    print_receipt(total, msg)

    # Mutable default trap check: two independent carts
    cart1 = add_to_cart("Book", 12.50)
    cart2 = add_to_cart("Pen", 2.00)
    print(cart1)  # [('Book', 12.5)]
    print(cart2)  # [('Pen', 2.0)]  -> separate lists

    # Build a cart and check out with a valid coupon
    cart = add_to_cart("Laptop", 1000)
    cart = add_to_cart("Mouse", 50, cart)
    total, msg = checkout(cart, "SAVE10")
    print_receipt(total, msg)

    # Invalid coupon
    total, msg = checkout(cart, "FAKE")
    print_receipt(total, msg)