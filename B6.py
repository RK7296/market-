def bond_price(face, coupon_rate, n, y):
    coupon = face * coupon_rate
    price = 0

    for t in range(1, n + 1):
        price += coupon / (1 + y)**t

    price += face / (1 + y)**n

    return price
price = bond_price(1000, 0.065, 5, 0.072)
print(price)

import numpy as np
import matplotlib.pyplot as plt

def bond_price(face, coupon_rate, n, y):
    coupon = face * coupon_rate
    price = 0

    for t in range(1, n + 1):
        price += coupon / (1 + y)**t

    price += face / (1 + y)**n

    return price


# Parameters from B5
face = 1000
coupon_rate = 0.065
n = 5

# Yield range: 2% to 12%
yields = np.linspace(0.02, 0.12, 100)

prices = [bond_price(face, coupon_rate, n, y)
          for y in yields]

# Plot
plt.plot(yields * 100, prices)
plt.xlabel("Yield (%)")
plt.ylabel("Bond Price (Rs.)")
plt.title("Bond Price vs. Yield")
plt.grid(True)
plt.show()