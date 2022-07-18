def dicvaluesum (mydic):
    list = []
    for i in mydic:
        list.append(mydic[i])
    final = sum(list)
    return final

mydic = {'a': 100, 'b': 200, 'c': 300}
print (dicvaluesum (mydic))
