def calculate(list):
    i = 0
    intab = []
    res = 0
    while i < len(list):
        if type(list[i]) == str:
            res = res + int(list[i])
        i += 1
    print(res)
    

calculate([3, '8', 1, '-1'])