for i in range(3):

    number = int(input("Enter an integer: "));
    if number > 0:
        print("%d is positive." % number);
    elif number < 0:
        print("%d is negative." % number);
    else:
        print("The number is zero.");

print("End of Process");

print("\n******************************\n");

i=0
while i<3:

    number = int(input("Enter an integer: "));
    if number > 0:
        print("%d is positive." % number);
    elif number < 0:
        print("%d is negative." % number);
    else:
        print("The number is zero.");
    i=i+1;

print("End of Process");

print("\n******************************\n");

answer = "y";
while answer=="y":

    number = int(input("Enter an integer: "));
    if number > 0:
        print("%d is positive." % number);
    elif number < 0:
        print("%d is negative." % number);
    else:
        print("The number is zero.");
    answer = input("Would You Like to Continue? (y/n): ");
    if answer != "y":
        if answer != "n":
            print("Invalid Entry\nEnd of Process");
    if answer == "n":
        print("End of Process");