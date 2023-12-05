def max_num_in_list(a_list):
    if not a_list:
        return None  # Return None for an empty list
    
    max_num = a_list[0]  # Initialize max_num with the first element of the list
    
    for num in a_list:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    
    return max_num

# Example usage:
my_list = [4, 7, 1, 9, 3, 5]
result = max_num_in_list(my_list)
print(f"The maximum number in the list is: {result}")