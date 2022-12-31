def unique(data):
    result = []
    for element in data:
        if element not in result:
            result.append(element)
    return result
