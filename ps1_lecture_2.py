# Problem Set 1 (From Lecture 2)
# Name: John Kautzner
# Collaborators:  None
# Time: 1:30
#

##balance = float(raw_input("Enter the outstanding balance on your credit card: "))
##annualIntRate = float(raw_input("Enter the annual interest rate as a decimal: "))
##minMonPayRate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
##intPaid = 0
##totalPaid = 0
##
##for month in range(1, 13):
##    print "Month ", month
##    
##    minMonPay = minMonPayRate*balance
##    minMonPay = float('%.2f' % minMonPay)
##    print "Minimum monthly payment: $", minMonPay
##
##    totalPaid += minMonPay
##    
##    intPaid = annualIntRate/12*balance
##    intPaid = float('%.2f' % intPaid)
##    
##    princPaid = minMonPay - intPaid
##    print "Principle paid: $", princPaid
##
##    balance = balance - princPaid
##    print "Remaining balance: $", balance
##
##print
##print "RESULT"
##print "Total amount paid: $", totalPaid
##print "Remaining balance: $", balance

balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annualIntRate = float(raw_input("Enter the annual interest rate as a decimal: "))
monIntRate = annualIntRate/12.0
monPayment = balance/12.0
months = 0

while balance > 0:
    balance = balance*(1+monIntRate)- monPayment
    months += 1

print "RESULT"
print "Monthly payment to pay off debt in 1 year: $", monPayment
print "Number of months needed: ", months
print "Balance: $", balance
