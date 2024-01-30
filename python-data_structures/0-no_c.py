def no_c(my_string):
    # Using list comprehension to create a new string without 'c' and 'C'
    result = ''.join(char for char in my_string if char not in ('c', 'C'))
    return result
