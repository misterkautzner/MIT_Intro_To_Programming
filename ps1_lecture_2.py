# Problem Set 1 (From Lecture 2)
# Name: John Kautzner
# Collaborators:  None
# Time: 0:00
#

balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annualIntRate = float(raw_input("Enter the annual interest rate as a decimal: "))
minMonPayRate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
intPaid = 0

for month in range(1, 13):
    print "Month ", month
    
    minMonPay = minMonPayRate*balance
    print "Minimum monthly payment: $", minMonPay
    
    intPaid = annualIntRate/12*balance
    princPaid = minMonPay - intPaid
    print "Principle paid: $", princPaid

    balance = balance - princPaid
    print "Remaining balance: $", balance
