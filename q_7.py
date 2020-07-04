# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

friends = [("Muskan", "Sharma", 22), ("Milan", "Shrestha", None), ("Sakar", "Ghimire", 24),("Kushal","Bhandari",None)]
count = 0
sum = 0
average = 0.0
for age in friends:
    if age[2]==None:
        count +=1
    else:
        sum = sum+age[2]

average = sum/(len(friends)-count)
print("the average age is: ",average)

for person_status in friends:
    if person_status[2]!=None:
        if person_status[2]>average:
            print(person_status[0], "is old")
        else:
            print(person_status[0], "is young")




