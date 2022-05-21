# Input Problems and fixes

# The below code does not work as the input function can only use a string by default

#anything = input("Enter a number: ")
#something = anything ** 2.0
#print(anything, "to the power of 2 is", something)

# To fix this however we use either int(string) or float(string)

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)