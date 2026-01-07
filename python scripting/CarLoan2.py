vehiclePrice = float(input("Enter Vehicle Price: "));
tradeInValue = float(input("Enter Trade-In Value: "));
downPayment = float(input("Enter Down Payment: "));
termOfLoan = int(input("Enter Term of Loan (Number of Months): "));
creditScore = int(input("Enter Credit Score: "));

if creditScore >=701:
    interest = 3;
elif 501 <= creditScore <= 700:
    interest = 5;
else:
    interest = 10;



totalPrice = float(vehiclePrice - tradeInValue - downPayment);
interestAmount = (interest/100)*totalPrice;
grandTotal = float( totalPrice + interestAmount);
monthlyPayment = float(grandTotal/termOfLoan);

print("Total Vehicle Price: $%.2f" % totalPrice);
print("Interest (%d percent): $%.2f" % (interest, interestAmount));
print("Grand Total: $%.2f" % grandTotal);
print("Monthly Payment: $%.2f" % monthlyPayment);
