# Lists basics note: first number starts at 0 count there [0, 1, 2 ,3, 4]

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nNew list content:", numbers)  # Printing new list content.

numbers[1] = numbers[4]  # Copying value of the fifth element (1) to the second (5).
print("\nNewer list content:", numbers)  # Printing Newer list content.

print("\nList length:", len(numbers))  # Printing the list's length.