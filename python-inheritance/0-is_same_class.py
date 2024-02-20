def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.

    :param obj: The object to check.
    :param a_class: The class to compare against.
    :return: True if obj is an instance of a_class, False otherwise.
    :rtype: bool
    """
    return type(obj) == a_class
