# 1
fname = "Tony"
lname = "Stark"
age = 51

if(fname=="Tony" , age>30):
    print("Tony is genius")

# Calculator

a=10 
b=3
s= input("Enter the operation : ")

if s == '+':
    r = int(a)+int(b)
elif s == '-':
    r = int(a)-int(b)
elif s == '*':
    r = int(a)*int(b)
elif s == '/':
    r = int(a)/int(b)
elif s == '%':
    r = int(a)%int(b)

print("For the Operation "+s," The result is "+str(r))
