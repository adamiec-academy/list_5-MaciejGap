def unique(data):
    result = []
    set_result = set()
    for element in data:
        if element not in set_result:
            result.append(element)
            set_result.add(element)
    return result
