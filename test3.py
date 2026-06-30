import random

print("hello", end=" ")
print("anjula..")
print("i'm", 25, "years old.") #this is a comment

x = str(4);
y = int(2);
z = float(2);

print(x, " ", y, " " , z, " ");
print(type(x))

a,b,c = "org","bana", "apple"

print(a, " ", b, " " , c, " ");
print("hello","world")


def myFunc():
    print(x, "this is a global var")


myFunc()

print(random.randrange(1,10))