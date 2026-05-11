x = int(input("Enter number :  "))
y = int(input("Enter number :  "))

if (x > 0 and y > 0):
    print("Q1")
else (x < 0 and y > 0):
    print("Q2")
else (x < 0 and y < 0):
    print("Q3")
else (x > 0 and y < 0):
    print("Q4")
else (x == 0 and y == 0):
    print("Origin")
else (y == 0 and x != 0):
    print("X-axis")
else (x == 0 and y != 0):
    print("Y-axis")
