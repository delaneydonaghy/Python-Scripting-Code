vehiclePrice = float(input("Enter Vehicle Price: "));
tradeInValue = float(input("Enter Trade-In Value: "));
downPayment = float(input("Enter Down Payment: "));
termOfLoan = int(input("Enter Term of Loan (Number of Months): "));

totalPrice = float(vehiclePrice - tradeInValue - downPayment);
monthlyPayment = float(totalPrice/termOfLoan);

print("Total Vehicle Price: $%.2f" % totalPrice);
print("Monthly Payment: $%.2f" % monthlyPayment);
