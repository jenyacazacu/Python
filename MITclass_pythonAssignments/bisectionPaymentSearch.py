#this is a program that calculates the min of fixed amount needed to pay of a loan
#the program implements bisection search to reduce the amount of steps it takes
import math
balance = 320000
annualIntereserRate = 0.2
minPayment=0
initialBalance=balance

#the lower bound is if there would be no interest and we pay 1/12 of the balance each month
monthlyLowerBound=balance/12.00
#the upper bound is if we would not make any paymnets and the interest would be accrued on the entire balance, the max possible
monthlyUpperBound=(balance*pow((1+(annualIntereserRate/12.00)),12))
e=1

while abs(initialBalance)>e:
    minPayment=(monthlyLowerBound+monthlyUpperBound)/2.00
    print("Min Payment:"+str(minPayment))
    initialBalance=balance
    i=1
    while i<=12:
        monthlyUnpaid=initialBalance-minPayment
        initialBalance=monthlyUnpaid + (monthlyUnpaid*(annualIntereserRate/12.00))
        i+=1
    if initialBalance>e:
        monthlyLowerBound=minPayment
    elif initialBalance<-e:
        monthlyUpperBound=minPayment
    
        

print("Lowest Payment:"+str(round(minPayment,2)))
print("Last Balance:"+str(initialBalance))