def calculate(list):
    i = 0
    intab = []
    res = 0
    if (type(list) != list):
        return False
    while i < len(list):
        if type(list[i]) == str:
            res = res + int(list[i])
        i += 1
    print(res)
    

calculate('8')