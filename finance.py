# Made by Jacobus Burger (2022)
# Personal finance functions for the fun of learning



##### PERSONAL FINANCE #####

def compound_interest(P, r, n, t):
    """calculate amount after compounding interest period"""
    return P * (1 + r/n)**(n*t)


def amortization(P, r, n, t):
    """
    calculate amortization over a period of time.
        P = principal
        r = interest rate
        t = number of periods
        n = payments per period
    """
    return (P * (r/n)) / (1 - (1 + r/n)**(-n*t))


# total return from mutual funds
def total_return(units,
        cost_per_unit,
        dividend_per_unit,
        interest_per_unit,
        closing_navps):
    opening   = units * cost_per_unit
    dividends = units * dividend_per_unit
    interest  = units * interest_per_unit
    closing   = units * closing_navps
    return ((closing - opening) + dividends + interest) / opening


# unrealized capital loss/gain over period
def unrealized_capital_loss_or_gain(units, beginning_navps, ending_navps):
    return (units * beginning_navps) - (units * ending_navps)


