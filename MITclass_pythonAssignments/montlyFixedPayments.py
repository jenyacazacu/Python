#this program calculates the payments on a loan over a 12 month period
#it uses a fixed payment schedule

balance = 320000
annualIntereserRate = 0.2
minPayment=0
initialBalance=balance

while initialBalance>0:
    minPayment+=10
    print("Min Payment:"+str(minPayment))
    initialBalance=balance
    i=1
    while i<=12:
        monthlyUnpaid=initialBalance-minPayment
        initialBalance=monthlyUnpaid + (monthlyUnpaid*(annualIntereserRate/12.00))
        i+=1
   

print("Lowest Payment:"+str(minPayment))
print("Last Balance:"+str(initialBalance))

