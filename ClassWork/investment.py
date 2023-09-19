investment_amount = int(input("ENTER AMOUNT YOU WANNA INVEST : "))
investment_percentage = 0.1
for year in range(1, 31):
    roi = investment_percentage * investment_amount
    investment_profit = investment_amount * (1 + investment_percentage)
    investment_amount = investment_profit
    print(f"YOUR ROI IS ${roi:.2f}, YOUR INVESTMENT IS NOW ${investment_profit:.2f} FOR YEAR {year}")