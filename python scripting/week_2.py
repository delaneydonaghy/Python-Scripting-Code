print("hello"); #double quotation are for string
print(123); #integer doesn't require quotation
print(123+4); #integer doesn't require quotation
print("123"+"4"); #string requires quotation
print(10.53); #decimal or real number is a float

a=100/3
print("%.2f" % a);   #this limits the float to 2 decimals and automatically rounds

print(int(a));    #makes it a whole number or integer
print( "%d" %(123/7)); #another way to make an integer and restricts to 32 btis
print("123 x 7 = %d" % (123*7));
print("%s" % "John"); #reserves string

print("%.2f" % (123/7));
print("$%.2f" % (123/7));
"""
this is a comment
in more than
one line
"""
 
print("My name is %s. I want to see the result of 123/7 = %.2f\nI want to see the resulit of 123*7 = %d." % ("john",(123/7), (123*7)));
