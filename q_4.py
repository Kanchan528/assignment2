# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

list1 = []
print(id(list1))
list1.append("Aruna")
list1.append("Nischal")
list1.append("Muskan")
list1.append("Bibek")
print(list1)
print(id(list1))
list1.sort()
print(list1)
print("The first item in the list is: ",list1[0] ,"and the second item in the list is: ",list1[1])
