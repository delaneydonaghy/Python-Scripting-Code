

while True:
    user_input = input("Please enter a number: ")
    try:
        number = float(user_input)
        break
    except ValueError:
        print("That is not a valid number, Please try agian. ");

print("You entered the number: %.2f" % number);

