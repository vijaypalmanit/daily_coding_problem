#Write an efficient function that takes stock_prices and returns the best #profit I could have made from one purchase and one sale of one share of #Apple stock yesterday.

#For example:

#  stock_prices = [10, 7, 5, 8, 11, 9,3]

#get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

def get_max_profit(stock_prices):
  min_price=stock_prices[0]
  max_profit=0
  for current_price in stock_prices:
    min_price=min(min_price,current_price)
    profit_so_far=current_price-min_price
    max_profit=max(max_profit,profit_so_far)

  return max_profit  

stock_prices = [10, 7, 5, 8, 11, 9,3]
print(get_max_profit(stock_prices))