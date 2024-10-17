def array_diff(a, b):  
    new_list = []
    for y in a:
        if y not in b:
            new_list.append(y)
    return new_list

print(array_diff([1,2,3],[1,2]))