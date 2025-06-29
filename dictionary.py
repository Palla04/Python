# In Python, a dictionary is a built-in data structure used to store data values 
# in key:value pairs. It is a collection that is ordered, changeable, and does not 
# allow duplicate keys.

marks = {"English" : 95, "Chem": 98, "Math": 99}
information = {"ram":"1786","Sam":"9875","ram":"9087"} 
print(information) # As dict does not allow duplicate keys so ignore the 2nd ram

print(marks["Chem"])

# Add new element
marks["Physics"] = 92
print(marks)

# update value
marks["English"] = 88
print(marks)