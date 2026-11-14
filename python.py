
def is_adult(age):
    if age <= 18:
        return False
    return True

print(is_adult(22))

def add(a,b):
    return a+b

def sub(c,d):
    return c-d

ans1 = add(12,13)
ans2 = sub(9,7)

print(ans1,ans2)

result1,result2 =add(11,12),sub(9,8)
print(result1,result2)

def add_to_cart(item,price,cart=None):
    if cart is None:
         cart =['book',200]
         return "nothing added to cart"
    return "added to cart"

print(add_to_cart('book',200))
