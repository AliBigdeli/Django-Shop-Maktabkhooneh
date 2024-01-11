

def cart_processor(request):
    cart = {
        "20": {
            "quantity":10,
            "price":3000
        }
    }
    return {"cart": cart}
