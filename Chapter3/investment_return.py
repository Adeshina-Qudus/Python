investment_amount = int(input("ENTER AMOUNT YOU WANT TO INVEST : "))
investment_percentage = 0.7
for investment_year in range(1, 31):
    investment_return = investment_amount * (1 + investment_percentage) ** investment_year

    print(f"THE AMOUNT RETURN FOR YEAR {investment_year} IS , {investment_return:.2f}")