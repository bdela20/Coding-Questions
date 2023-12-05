def is_consecutive(a_list):
    if not a_list or len(a_list) < 2:
        return False
    
    sorted_list = sorted(a_list)

    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1] + 1: 
            return False
        
    return True

print(is_consecutive([2,3,4,5,6,7]))
print(is_consecutive([1,4,5]))