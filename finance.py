# Made by Jacobus Burger (2022)
# Various finance maths

def compound_interest(P, r, n, t):
  return P * (1 + r/n)**(n*t)
