from graphics import *

canvas = GraphWin("Canvas", 600, 800);

p1 = Point(10,10);
p1.draw(canvas);

p2 = Point(300,200);
p2.draw(canvas);

circle = Circle(p2, 30); #30 is radius, p2 is the location
circle.draw(canvas);
circle.setFill("yellow");

circle2 = Circle(p2, 20);
circle2.setFill("blue");
circle2.draw(canvas);


circle3 = Circle(p2, 10);
circle3.setFill("green");
circle3.draw(canvas);


p4 = Point(300,100);
p5 = Point(500,200);
p4.draw(canvas);
p5.draw(canvas);

rectangle = Rectangle(p4,p5);
rectangle.draw(canvas);
rectangle.setFill("pink");

a = Point(200,400);
b = Point(50,500);
c = Point(125,625);
d = Point(275,625);
e = Point(350,500);

polygon = Polygon(a,b,c,d,e);
polygon.draw(canvas);
polygon.setFill("purple");

label = Text(p2, "Hello");
label.draw(canvas);
label.setFill("white");

