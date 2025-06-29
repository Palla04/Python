student = ["Radha","Raseswari","Ramma","Sarbadda","Gopi"]
#In Python, break and continue are control flow statements used within loops (for and while) to 
# alter their normal execution.

# break
print("Using Break : ")
for name in student:
    if name == 'Sarbadda':
        break   #The break statement immediately terminates the loop in which it is executed.
    print(name)

# continue
print("Using Continue : ")
for name in student:
    if name == 'Sarbadda':
        continue  #The continue statement skips the current iteration of the loop and proceeds to the next iteration.
    print(name)