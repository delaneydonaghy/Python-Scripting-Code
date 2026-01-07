def ComputeAreaOfTriangle():
    areaOfTriangle = 5*10*(1/2);
    print(areaOfTriangle);


def AreaOfTriangle(base, height):
    areaOfTriangle = base*height*(1/2);
    print("%.1f" % areaOfTriangle);


base2 = float(input("Enter the Triangle's Base: "));    
height2 = float(input("Enter the Triangle's Height: "));

AreaOfTriangle(base2, height2);

def AreaOfTriangleResults(base, height):
    areaOfTriangle = base*height*(1/2);
    return areaOfTriangle;

print(AreaOfTriangleResults(15,10));

x = AreaOfTriangleResults(15,10);

def setList(list1):
    print(list1);
def combineList(list1, list2):
    return list1+list2;

list_of_Items = eval(input("Please Enter a List of Items: "));
list_of_Numbers = eval(input("Please Enter a List of Numbers: "));

setList(list_of_Items);

print(combineList(list_of_Items, list_of_Numbers));