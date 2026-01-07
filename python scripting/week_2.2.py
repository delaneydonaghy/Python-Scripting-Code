firstName = input("Enter First Name: ");
lastName = input("Enter Last Name: ");
prefix = input("Enter Prefered Suffix: ");
month = int(input("Enter Month: "));
day = int(input("Enter Day: "));
year = int(input("Enter Year: "));
date = ("%d/%d/%d" % (month, day, year));
salary = float(input("Enter Salary: "));
position = input("Enter Job Position: ");
status = input("Enter Employment Status: ");
_5PercentIncrease = salary *1.05;



print("Dear Sir or Madam:");
print("\n\nThis letter is to confirm that " + firstName + " " + lastName + " is presently employed by ABC Company, in the ");
print("position of "+position+" on a "+status+" basis. "+firstName+" "+lastName+" commenced employment with ");
print("company on "+date+" and is presently paid $%.2f based salary per year." % salary);
print("\n\n Employee will recieve a new salary on October 31, 2024 due to 5 percent increase and it is $%.2f." % _5PercentIncrease);
print("\n\nABC company is located at 100 N Street, Arlington, VA, 22207.");
print("\n\nIf you require any addtional information about ABC company and/or "+prefix+"."+lastName+", please do not ");
print("hesitate to contact us.\n\nSincerely,\n\n\n");
