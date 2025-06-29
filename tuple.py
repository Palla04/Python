# A tuple in Python is an ordered and immutable collection of elements. 
# This means that once a tuple is created, its elements cannot be changed, 
# added, or removed. Tuples are similar to lists but differ in their mutability. 

result = (95,97,96,98,97,92)
# result[1] = 99  as tuble is immutable so we can't modify
print(result)
print(result.count(97)) # 2
print(result.index(97)) # first position 1

print(result[-1])  # 92

# use loop in tuple 
for item in result:
    print(item, end=' ')

print()

# we can also write tuple as
person = "ram","sam","jaddu","madhu" # by default it is a tuple
print(person)                        # [], (), {}
