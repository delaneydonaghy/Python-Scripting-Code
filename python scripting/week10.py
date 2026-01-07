list_of_names = eval(input("Please Enter Five Names: "));
print(list_of_names);
print("Second Name in the list: " + list_of_names[1]);

L1 = [1,2,3];
L2 = [4,5,6];
L3 = L1 + L2;
print(L3);

len(L1);
len(L2);
len(L3);

print(max(L3));
print(min(L3));

for index in range(len(L3)):
    print(L3[index]+10);

print("Total: %d" % sum(L3));