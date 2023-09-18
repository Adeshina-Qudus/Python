name = (input("ENTER YOUR NAME TO PRINT YOUR PAYROLL STATEMENT : "))
name1 = (input("Employee Name : "))
hours = float(input("Enter numbers of Hours Worked in a week : "))
pay_rate = float(input("Enter hourly pay rate : "))
month = (input("Enter month : "))
federal_tax_withholding_rate = float(input("Enter your federal tax withholding rate : "))
state_tax_withholding_rate = float(input("Enter your state tax withholding rate : "))

gross_pay = pay_rate * hours
federal_tax_withholding_rate1 = (federal_tax_withholding_rate / 100) * gross_pay
state_tax_withholding_rate1 = (state_tax_withholding_rate / 100) * gross_pay
total_deduction = federal_tax_withholding_rate1 + state_tax_withholding_rate1
net_total = gross_pay - total_deduction


print(name, "Payroll statement for the month of", month)
print("Employee Name: ", name1)
print("Hours Worked: ", hours)
print("Pay Rate: ", pay_rate)
print("Gross Pay: ", gross_pay)
print("Deductions:")
print("Federal Withholding", "(",federal_tax_withholding_rate,"%):", federal_tax_withholding_rate1)
print("State Withholding ", "(",state_tax_withholding_rate,"%):", state_tax_withholding_rate1)
print("Total Deduction: ", total_deduction)
print("Net Pay:", net_total)