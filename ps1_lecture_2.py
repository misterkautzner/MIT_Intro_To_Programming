# Problem Set 1 (From Lecture 2)
# Name: John Kautzner
# Collaborators:  None
# Time: 2:30
#
#Problem 1:   Calculate the credit card balance after one year if a person only pays the
#minimum monthly payment required by the credit card company each month.

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



#Problem 2:  Calculate the minimum fixed monthly payment (increments of $10) needed in order pay
#off a credit card balance within 12 months

##newBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
##annualIntRate = float(raw_input("Enter the annual interest rate as a decimal: "))
##monIntRate = annualIntRate/12.0
##monPayment = int(newBalance/12)/10*10
##balance = newBalance
##
##while balance > 0:  #Calculate balance after 12 months until we find the minimum monthly payment that reduces balance to no greater than 0 in that time.
##    
##    for i in range(1, 13):
##        balance = float('%.2f' % (balance*(1+monIntRate)- monPayment))
##        
##        if(balance <= 0): #When the balance is cleared, we're done.
##            months = i
##            break
##
##    if(balance > 0):    #After 12 months, if balance is still positive, we need to restart the while loop with updated monPayment.
##        monPayment += 10
##        balance = newBalance
##
##
##print "RESULT"
##print "Monthly payment to pay off debt in 1 year: $", monPayment
##print "Number of months needed: ", months
##print "Balance: $", balance





#Problem 3:  Calculate the minimum fixed monthly payment (to the nearest cent) needed in order pay
#off a credit card balance within 12 months

newBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
annualIntRate = float(raw_input("Enter the annual interest rate as a decimal: "))
monIntRate = annualIntRate/12.0
lbound = float(newBalance/12.0)
ubound = float((newBalance*(1 + annualIntRate/12.0)**12.0)/12.0)
monPayment = float('%.2f' % ((lbound + ubound)/2.0))
balance = newBalance
finished = 2

#Calculate balance after 12 months until we find the minimum monthly payment that reduces balance to no greater than 0 in that time.
while finished != 0:  #Terminates after 1 iteration once lbound and ubound are within 1 cent of each other.
    balance = newBalance
    
    for months in range(1, 13):
        balance = float('%.2f' % (balance*(1+monIntRate)- monPayment))
        
        if(balance <= 0): #When the balance is cleared, we're done with this loop
            break

#Bisection method to find the right payment
    if(balance > 0):
        lbound = monPayment

    elif(balance < 0):
        ubound = monPayment

    else:
        lbound = monPayment
        ubound = monPayment

    if(ubound - lbound <= .01):
        finished -= 1
        
    monPayment = float('%.2f' % ((lbound + ubound + .001)/2.0))
    print "lbound: ", lbound, "  monPayment: ", monPayment, "  ubound: ", ubound

print "RESULT"
print "Monthly payment to pay off debt in 1 year: $", monPayment
print "Number of months needed: ", months
print "Balance: $", balance
