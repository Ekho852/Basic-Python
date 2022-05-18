#Keyword argument "sep" ie separator and "end"
#line 4 prints "My name is" which is then separated by "_" and connects line 5 starting with "*"
#line 5 prints "Monthy Python" which is then separated by "*" and connects the next line starting with "*" and a space

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#Any keyword arguments have to be put after the last positional argument