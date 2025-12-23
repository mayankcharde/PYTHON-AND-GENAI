tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea for tea, price in tea_prices_inr.items()}
tea_prices_usd1 = {tea:price / 80 for tea, price in tea_prices_inr.items()}
tea_prices_usd2 = {price for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
print(tea_prices_usd1)
print(tea_prices_usd2)