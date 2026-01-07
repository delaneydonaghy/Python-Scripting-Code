
for q in range(5):
    print("\nDelivery Service");

    distance = int(input("Enter Distance (1) Local - (2) Long Distance: "));
    weight = float(input("Enter Weight: "));

    if distance == 1:
        i="Local"
    elif distance == 2:
        i= "Long Distance"

    if distance == 1:
        if weight < 5:
            fee = 12.00;
        elif 5 <= weight <= 20:
            fee = 16.50;
        elif weight > 20:
            fee = 22.00;

    if distance == 2:
        if weight < 5:
            fee = 35.00;
        elif weight >= 5:
            fee = 47.95;

    print("------Summary------");

    print("Delivery Type: %s" % i);
    print("Weight: %.1f pounds" % weight);
    print("Fee: $%.2f" % fee);

    print("-------------------");
