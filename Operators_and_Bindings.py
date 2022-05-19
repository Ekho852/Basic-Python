# Operators and Bindings
# The binding of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression.

# Python follows BEMDAS like real life maths

print(2 + 3 * 5)
print()

# Python is typically left side binding as the below would cause an error if right sided
# ie (6%2) = 0 -> (9%0) = error
print(9 % 6 % 2)