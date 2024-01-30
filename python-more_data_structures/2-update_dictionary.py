def update_dictionary(a_dictionary, key, value):
    # Create a new dictionary with the original content
    new_dict = dict(a_dictionary)

    # Update the value for the given key in the new dictionary
    new_dict[key] = value

    return new_dict

def print_sorted_dictionary(my_dict):
    """Print sorted dictionary"""
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))
