average_price = 600
discount_threshold = 0.7 
critical_stock_level = 30 
normal_order_quantity = 15 
minimum_order_quantity = 5

current_price = int(input("Enter Current Price: "))  
current_stock = int(input("Enter Current Stock: "))

def decide_order(current_price, current_stock):

    discounted_price = average_price * (1 - discount_threshold)
    tobuy = 0
    
    if (current_price < discounted_price) and current_stock < critical_stock_level:
        tobuy = normal_order_quantity

    elif current_stock < 10:
        tobuy = minimum_order_quantity

    else:
         tobuy = 0

    return tobuy

tobuy = decide_order(current_price, current_stock)

if tobuy > 0:
    print(f"Agent decides to order {tobuy} units.")
else:
    print("Agent decides not to place an order.")
