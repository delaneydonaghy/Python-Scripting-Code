number = int(input("Please enter an integer: "));
print("You have entered: %d" % number);

if number > 0:
    print("%d is a positive integer" % number);

elif number <0:
    print("%d is a negative integer" % number);

elif number==0:
    print("%d is neither positive nor negative" % number);

else:
    print("Error: You have not entered a valid number");