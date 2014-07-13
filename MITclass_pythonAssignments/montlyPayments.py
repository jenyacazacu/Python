#this program calculates the payments on a loan over a 12 month period
#test case
balance = 4842
annualIntereserRate = 0.2
monthlyPaymentRate = 0.04
i=1
totalPaid=0
monthlyUnpaid=balance

while i<=12:
    print("Month:"+str(i))
    payment = balance*monthlyPaymentRate
    print("Minimum Montlhy payment:"+str(round(payment,2)))
    totalPaid+=payment
    monthlyUnpaid=balance-payment
    balance=monthlyUnpaid + (monthlyUnpaid*(annualIntereserRate/12.00))
    print("Remaining Balance:"+str(round(balance,2)))
    i+=1
    
print("Total Paid:"+str(round(totalPaid,2)))
print("Remaining Balance:"+str(round(balance,2)))