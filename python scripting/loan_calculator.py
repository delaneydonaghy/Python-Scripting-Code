firstName = input("Enter First Name: ");
lastName = input("Enter Last Name: ");
address = input("Enter Billing Address: ");
loan = float(input("Enter Loan Amount: "));
term = int(input("Enter Term of Loan (Number of Months to Pay off): "))

interest_amount = loan*.039;
total_loan = loan+interest_amount;
payment = total_loan/term;

print("\nBorrower: "+firstName+" "+lastName+"");
print("Billing Address: "+address+"");
print("Loan Amount: $%.2f" % loan);
print("Interest: $%.2f" % interest_amount);
print("Total Loan Amount: $%.2f" % total_loan);
print("Term of Loan: %d" % term);
print("Monthly Payment: $%.2f" % payment);

