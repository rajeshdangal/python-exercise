# Prices of 10 products
prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]

total_sum = 0

while True:

    print("Please select product (1-10) 0 to Quit: ", end="")
    product_number = input().strip()

    if product_number == "0":
        break
    elif product_number.isdigit() and 1 <= int(product_number) <= 10:
        price = prices[int(product_number) - 1]
        total_sum += price
        print(f"Product: {product_number} Price: {price}")
    else:
        print("Incorrect selection.")

print(f"Total: {total_sum}")

payment = int(input("Payment: ").strip())
change = payment - total_sum

print(f"Change: {change}")
