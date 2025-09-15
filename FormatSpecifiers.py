price1 = 3000.14159
price2 = -9802.56
price3 = 1200.8

# .(number)f = round to that many decimal places (fixed point)
print(f"Your price1 is: {price1:.2f}")
print(f"Your price2 is: {price2:.2f}")
print(f"Your price3 is: {price3:.2f}")
print("-----------------------------")

# :(number) = allocate that many spaces
print(f"Your price1 is: {price1:10}")
print(f"Your price2 is: {price2:10}")
print(f"Your price3 is: {price3:10}")
print("-----------------------------")

# :03 = allocate and zero pad that many spaces
print(f"Your price1 is: {price1:010}")
print(f"Your price2 is: {price2:010}")
print(f"Your price3 is: {price3:010}")
print("-----------------------------")

# :< = left justify
print(f"Your price1 is: {price1:<10}")
print(f"Your price2 is: {price2:<10}")
print(f"Your price3 is: {price3:<10}")
print("-----------------------------")

# :> = right justify
print(f"Your price1 is: {price1:>10}")
print(f"Your price2 is: {price2:>10}")
print(f"Your price3 is: {price3:>10}")
print("-----------------------------")

# :^ = center align
print(f"Your price1 is: {price1:^10}")
print(f"Your price2 is: {price2:^10}")
print(f"Your price3 is: {price3:^10}")
print("-----------------------------")

# :+ = use a plus sign to indicate positive value
print(f"Your price1 is: {price1:+10}")
print(f"Your price2 is: {price2:+10}")
print(f"Your price3 is: {price3:+10}")
print("-----------------------------")

# := = place sign to leftmost position
print(f"Your price1 is: {price1:=+10}")
print(f"Your price2 is: {price2:=+10}")
print(f"Your price3 is: {price3:=+10}")
print("-----------------------------")

# : = insert a space before positive numbers
print(f"Your price1 is: {price1: }")
print(f"Your price2 is: {price2: }")
print(f"Your price3 is: {price3: }")
print("-----------------------------")

# :, = comma separator
print(f"Your price1 is: {price1:,}")
print(f"Your price2 is: {price2:,}")
print(f"Your price3 is: {price3:,}")
print("-----------------------------")

# You can combine multiple format specifiers
print(f"Your price1 is: {price1:^10,.2f}")
print(f"Your price2 is: {price2:^10,.2f}")
print(f"Your price3 is: {price3:^10,.2f}")
print("-----------------------------")

