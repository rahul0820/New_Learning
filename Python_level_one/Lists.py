# Basic List
mylist =["string",1,2,3,4,5,True, [1,2,3]]
print(mylist)

# checking length of list
mylist = [1,2,3,4,5]
print(len(mylist))

# Reassiments
mylist=['a','b','c','d','e']
print("before reassignment")
print(mylist)
mylist[0] ="new item"
print("After reassignment")
print(mylist)

# Adding new item to end of list
mylist=['a','b','c','d','e']
mylist.append("new item")
print(mylist)

# addition of extension of list
mylist=['a','b','c','d','e']
newlist=['x','y','z']
mylist.extend(newlist)
print(mylist)

# removing items from list
mylist=['a','b','c','d','e']
mylist.pop(2)
print(mylist)

# Reverse Method
mylist=['a','b','c','d','e']
mylist.reverse()
print(mylist)

# sort method
mylist=[4,3,2,5,1]
mylist.sort()
print(mylist)

# Nested list
mylist=[1,2,['x','y','z']]
print(mylist[2])
print(mylist[2][1])

# List Comprehensions
matrix =[[1,2,3],[4,5,6],[7,8,9]]
first_col=[row[0] for row in matrix]
print(first_col)