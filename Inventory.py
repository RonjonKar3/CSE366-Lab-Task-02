average_price = 600
discount_threshold = 0.2 
critical_stock_level = 10 
normal_order_quantity = 15 
minimum_order_quantity = 10 

current_price = int(input("Enter Current Price: "))  
current_stock = int(input("Enter Current Stock: "))

def decide_order(current_price, current_stock):

    discounted_price = average_price * (1 - discount_threshold)
    order_quantity = 0
    
    # Place a larger order if there's a discount and stock is not critically low
    if (current_price <= discounted_price) and current_stock >= critical_stock_level:
        order_quantity = normal_order_quantity

    # Place a minimum order if stock is critically low
    elif current_stock < critical_stock_level:
        order_quantity = minimum_order_quantity

    return order_quantity

order_quantity = decide_order(current_price, current_stock)

if order_quantity > 0:
    print(f"Agent decides to order {order_quantity} units.")
else:
    print("Agent decides not to place an order.")