name = input("Enter Student's Full Name: ");
grades = eval(input("Enter 5 Test Scores between 0 and 100(Use commas to separate each score): "));

print("--------------- GRADE REPORT ---------------");
print("You entered the following test scores: ");


for index in range(len(grades)):
    print(grades[index]);

print("Hightest Score: %d" % max(grades));
print("Lowest Score: %d" % min(grades));

avg_score = (sum(grades)/len(grades))
print("Average Score: %.1f" % avg_score);

if avg_score > 60:
    print("%s passes the exam. " % name);
else:
    print("%s fails the exam. " % name);

if avg_score > 90:
    letter_grade = "A";
elif avg_score > 80:
    letter_grade = "B";
elif avg_score > 70:
    letter_grade = "C";
elif avg_score > 60:
    letter_grade = "D";
else:
    letter_grade = "F";

print("%s's Final Grade: %s" % (name, letter_grade));
print("-----------------------------------------");