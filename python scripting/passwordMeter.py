print("Simple Password Meter");
print("**************************");
passwd = input("Enter a New Password: ");
print("**************************");

score = 0;

if len(passwd) >= 8:
    score += len(passwd);
    print("Points for the Length of the Password: %d" % score);
    print("Points for Each Character:");
    for index in range(len(passwd)):
        if(90 >= ord(passwd[index]) >= 65):
            score += 2;
            print("%s = 2 points" % passwd[index]);
        elif(122 >= ord(passwd[index]) >= 97):
            score += 1;
            print("%s = 1 point" % passwd[index]);
        elif(57 >= ord(passwd[index]) >= 48):
            score += 3;
            print("%s = 3 point" % passwd[index]);
        else:
            score += 7;
            print("%s = 7 points" % passwd[index]);

else:
    print("A password must be 8 characters or more.");

print("Total Score: %d" % score);
print("**************************");

if(score>=50):
    strength = "Very Strong";
elif(40 <= score):
    strength = "Strong";
elif(30 <= score):
    strength = "Fair";
elif(20 <= score):
    strength = "Poor";
else:
    strength = "Very Poor";

print("Password Strength: %s" % strength);