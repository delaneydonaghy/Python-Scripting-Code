name = input("Enter Employee's Name: ");
hours = int(input("Enter Number of Hours Worked in a Week: "));
hourly = float(input("Enter Hourly pay rate: "));
fed_tax = float(input("Enter Percentage of Federal Tax Withholding: "));
state_tax = float(input("Enter Percentage of State Tax Withholding: "));

gross_pay = float(hours*hourly);
fed_withholding = (fed_tax/100)*gross_pay;
state_withholding = (state_tax/100)*gross_pay;
deduction = fed_withholding+state_withholding;
net_pay = gross_pay - deduction;

print("\nPayroll Statement");
print("Employee Name: %s" % name);
print("Hours Worked: %d" % hours);
print("Pay Rate: $%.2f" % hourly);
print("Gross Pay: $%.2f" % gross_pay);
print("Deduction");
print("- Federal Withholding (%.1f) percent: $%.2f"% (fed_tax, fed_withholding));
print("- State Withholding (%.1f) percent: $%.2f"% (state_tax, state_withholding));
print("- Total Deduction: $%.2f" % deduction);
print("Net Pay: $%.2f"% net_pay);
