# Define a function to check if all elements in a list are positive
def all_positive(numbers):
    if not numbers:  # Check if the input list is empty
        return "The list is empty."

    # Use the all() function to check if all numbers are greater than 0
    are_all_positive = all(number > 0 for number in numbers)

    if are_all_positive:  # Return a message based on the result
        return "All numbers are positive."
    else:
        return "Not all numbers are positive."

# List of numbers to test
test_numbers = [1, 2, 3, 4, 5]  # This list contains all positive numbers

result = all_positive(test_numbers) # Call the function and store the result

print(result) # Print the result

test_numbers_with_negatives = [1, -2, 3, 4, 5] # Test with a list that includes negative numbers

# Call the function again with the new list
result_with_negatives = all_positive(test_numbers_with_negatives)

print(result_with_negatives) # Print the result for the second test