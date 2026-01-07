
totalLocal = 0;
totalLong = 0;
totalLocalFee = 0;
totalLongFee = 0;


while(1==1):
    print("\nDelivery Service");

    distance = int(input("Enter Distance (1) Local - (2) Long Distance: "));
    weight = float(input("Enter Weight: "));

    

    if distance == 1:
        i="Local"
        totalLocal = totalLocal +1;
    elif distance == 2:
        i= "Long Distance"
        totalLong = totalLong + 1;

    if distance == 1:
        if weight < 5:
            fee = 12.00;
        elif 5 <= weight <= 20:
            fee = 16.50;
        elif weight > 20:
            fee = 22.00;
        totalLocalFee = totalLocalFee + fee;

    if distance == 2:
        if weight < 5:
            fee = 35.00;
        elif weight >= 5:
            fee = 47.95;
        totalLongFee = totalLongFee + fee;

    print("------Summary------");

    print("Delivery Type: %s" % i);
    print("Weight: %.1f pounds" % weight);
    print("Fee: $%.2f" % fee);

    print("-------------------\n");

    answer = input("(1) to continue : (0) to exit: ");
    if answer == "1":
        continue
    elif answer == "0":
        break
    else: 
        print("Invalid Entry!!")
        break

totalFee = totalLongFee + totalLocalFee;

print("\nFinal Report");
print("- Local Delivery: %d item(s)" % totalLocal);
print("- Total Local Delivery Fee: $%.2f" % totalLocalFee);
print("- Long Distance Delivery: %d item(s)" % totalLong);
print("- Total Long Distance Delivery Fee: $%.2f" % totalLongFee);
print("Total Fee: $%.2f" % totalFee);
print("Thank you. End of Delivery Service Application.");
