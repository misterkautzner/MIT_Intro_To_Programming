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

newBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
annualIntRate = float(raw_input("Enter the annual interest rate as a decimal: "))
monIntRate = annualIntRate/12.0
monPayment = int(newBalance/12)/10*10
print monPayment
balance = newBalance

while balance > 0:  #Calculate balance after 12 months until we find the minimum monthly payment that reduces balance to no greater than 0 in that time.
    #print monPayment
    
    for i in range(1, 13):
        balance = float('%.2f' % (balance*(1+monIntRate)- monPayment))
        
        if(balance <= 0): #When the balance is cleared, we're done.
            months = i
            break

    if(balance > 0):    #After 12 months, if balance is still positive, we need to restart the while loop with updated monPayment.
        monPayment += 10
        balance = newBalance


print "RESULT"
print "Monthly payment to pay off debt in 1 year: $", monPayment
print "Number of months needed: ", months
print "Balance: $", balance
