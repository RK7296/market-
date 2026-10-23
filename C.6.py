def bootstrap_zero_rates(par_yields):
    zero_rates = {}

    for n in range(1, len(par_yields) + 1):
        coupon = par_yields[n - 1]

        if n == 1:
            zero_rates[1] = coupon
        else:
            pv_coupons = 0

            for t in range(1, n):
                pv_coupons += coupon / (1 + zero_rates[t])**t

            remaining_pv = 1 - pv_coupons

            zero_rates[n]= (1 / remaining_pv) ** (1 / n) - 1

    return zero_rates


par_yields = [0.0520, 0.0545, 0.0560, 0.0570]

zero_rates = bootstrap_zero_rates(par_yields)

for maturity, rate in zero_rates.items():
    print(maturity, rate)
    
    
