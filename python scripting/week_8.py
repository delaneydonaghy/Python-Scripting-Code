#str = "hello";

#print(str[0]);

#print(str[4]);

#print(len(str));

#print(str.upper());
#print(str.lower());

input1 = input("Enter First String: ");
input2 = input("Enter Second String: ");

if(len(input1)==len(input2)):
    print("The inputs are the same length");
elif(len(input1)>len(input2)):
    print("The first input has a greater number of characters");
else:
    print("The second input has a greater number of characters");

print("Are the two strings equivalent?", (input1==input2));

print(input1[len(input1)-2]);