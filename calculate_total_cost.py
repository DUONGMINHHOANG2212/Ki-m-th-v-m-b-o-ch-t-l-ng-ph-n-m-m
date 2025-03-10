def calculate_total_cost(unit_price, quantity):
    if not (1000 <= unit_price <= 800000 and 1 <= quantity <= 1500):
        return "invalid input"
    
    shipping_fee = 40000  
    total_cost = unit_price * quantity  
    
    if quantity > 800:
        total_cost *= 0.65  
        shipping_fee = 0    
    elif quantity > 500:
        total_cost *= 0.80  
    
    total_cost += shipping_fee
    
    return int(total_cost)  
