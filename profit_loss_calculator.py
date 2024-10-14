def calculate_profit(cost_price, selling_price):
    """
    Calculate the profit based on the cost price and selling price.

    Args:
        cost_price (float): The cost price of the item.
        selling_price (float): The selling price of the item.

    Returns:
        float: The profit amount.
    """
    if cost_price < 0 or selling_price < 0:
        raise ValueError("Cost price and selling price must be non-negative numbers")

    profit = selling_price - cost_price
    return profit

def calculate_loss(cost_price, selling_price):
    """
    Calculate the loss based on the cost price and selling price.

    Args:
        cost_price (float): The cost price of the item.
        selling_price (float): The selling price of the item.

    Returns:
        float: The loss amount.
    """
    if cost_price < 0 or selling_price < 0:
        raise ValueError("Cost price and selling price must be non-negative numbers")

    loss = cost_price - selling_price
    return loss

def determine_profit_or_loss(cost_price, selling_price):
    """
    Determine whether there is a profit or loss based on the cost price and selling price.

    Args:
        cost_price (float): The cost price of the item.
        selling_price (float): The selling price of the item.

    Returns:
        str: A message indicating whether there is a profit, loss, or no profit/loss.
    """
    if selling_price == cost_price:
        return "No profit nor Loss"
    elif selling_price > cost_price:
        profit = calculate_profit(cost_price, selling_price)
        return f"Profit of {profit}"
    else:
        loss = calculate_loss(cost_price, selling_price)
        return f"Loss of {loss}"

# Driver Code
if __name__ == "__main__":
    try:
        cost_price = float(input("Enter the cost price: "))
        selling_price = float(input("Enter the selling price: "))

        result = determine_profit_or_loss(cost_price, selling_price)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
