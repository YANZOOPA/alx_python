"""writing a fonction  for the task Exact same object """
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.

    :param obj: The object to check.
    :param a_class: The class to compare against.
    :return: True if obj is an instance of a class that inherited from a_class, False otherwise.
    :rtype: bool
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
