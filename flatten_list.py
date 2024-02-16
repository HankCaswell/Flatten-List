def flatten(lst):
    if not isinstance(lst, list):
        return [lst]
    result = []
    for item in lst:
        if isinstance(item, list):
            # Recursively flatten the item if it is a list
            result.extend(flatten(item))
        else:
            result.append(item)
    return result