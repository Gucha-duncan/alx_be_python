monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_interest_rate = 0.05
time = 12
projected_annual_savings = (monthly_savings * time) + (monthly_savings * time * annual_interest_rate)
print("Projected savings after one year, with interest, is:", projected_annual_savings)