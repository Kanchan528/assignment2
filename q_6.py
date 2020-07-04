# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

friends = ["Ram", "Sita", "Krishna", "Biplab", "John"]

for name in friends:
    if name=="John":
        print("Found")
    else:
        print("Not found.")