# List is a collection of item, in other words it is used to store multiple items in a single variable.
# list is a complex datatype, it is ordered(the elements in a list maintain a specific order,) 
# and mutable(after creation we can modify it) collection of elements.

marks = [95, 92, 98, 97,"math"]
print(marks[0])  #95
print(marks[-1])  #97 (last item)
print(marks[-2])  #98

print(marks[0:-1])  #before last one

# for loop in List
for score in marks:
    print(score)

# append
marks.append(100)
print(marks)

# insert at particular index
marks.insert(1, 82)
print(marks)

# Checking
print(82 in marks)

# remove
marks.remove(97)
print(marks)

# length
print("Length of the list : ",len(marks))

# while loop
i=0
while i < len(marks):
    print(marks[i])
    i=i+1

# make the list Empty
marks.clear()
print(marks)



