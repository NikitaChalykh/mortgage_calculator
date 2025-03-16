def mortgage_calculator(obj, price, deposit, term=None):
    # Proportion to determine the annual interest rate
    ratio = ((int(price) - int(deposit)) - obj.payment_min) / (
        obj.payment_max - obj.payment_min
    )
    # Annual interest rate on the loan
    rate = obj.rate_min + (obj.rate_max - obj.rate_min) * ratio
    if term is None:
        return rate
    # Monthly interest rate on the loan
    month_rate = rate / 1200
    # Total loan rate
    global_rate = (1 + month_rate) ** (int(term) * 12)
    # Calculate annuity payment
    return ((int(price) - int(deposit)) * month_rate * global_rate) / (
        global_rate - 1
    )
