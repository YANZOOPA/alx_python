def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None
    
    # Initialize variables to store the best score and key
    best_score_value = float('-inf')  # Initialize with negative infinity to ensure any value is greater
    best_score_key = None

    # Iterate through key-value pairs in the dictionary
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the current best score
        if value > best_score_value:
            best_score_value = value
            best_score_key = key

    return best_score_key
