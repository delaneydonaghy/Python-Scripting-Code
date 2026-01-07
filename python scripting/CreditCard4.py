creditNumber = input("Enter Credit Card Number: ");
limit = float(input("Enter Credit Limit: "));

balance = 0;

while 1==1:
    charge = float(input("Enter Charge: "));
    balance = balance + charge;
    
    i=0;
    while(i==0):
        answer = input("Enter N for Next Charge OR Enter E to End: ");
        if answer == "N":
            i=1;
        elif answer =="E":
            i=1;
        else:
            print("Wrong Choice: Please Re-Enter!!!");
            continue;
    if answer == "N":
        continue;
    if answer =="E":
        break;


available = limit-balance;
if available <0:
    available = 0;

minPayment = balance*.025;

print("\nAccount Summary");
print("Credit Card: %s" %creditNumber);
print("Credit Limit: $%.2f" % limit);
print("Current Balance: $%.2f" % balance);
print("Available Credit: $%.2f" % available);
print("Minimum Payment Due: $%.2f" % minPayment);

