'''
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:
For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.
'''

income = 45000
tax = 0

if income <= 10000:
    tax += 0
elif income <= 20000:
    tax = (income - 10000) * 10 / 100
elif income > 20000:
    tax = ((income - 20000) * 20 / 100) + 1000

print(tax)
