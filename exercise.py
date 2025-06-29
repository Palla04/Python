# 1
fname = "Tony"
lname = "Stark"
age = 51

if(fname=="Tony" , age>30):
    print("Tony is genius")

# Calculator

a = input("Enter the first num: ") 
b = input("Enter the second num: ")
s= input("Enter the operator (+,-,*,/,%): ")

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

print("a "+s," b The result is "+str(r))
