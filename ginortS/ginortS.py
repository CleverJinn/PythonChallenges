def ginortS(S):  
    Upperletters = []
    Lowerletters = []
    
    numbers = []
    Even_num = []
    Odd_num = []
    
    ginort = ''
    
    for x in S:
        if x.isupper():
            Upperletters.append(x)
        elif x.islower():
            Lowerletters.append(x)
        elif x.isdigit():
            numbers.append(x)
            
    Lowerletters.sort()
    Upperletters.sort()
    numbers.sort()
    
    for x in numbers:
        if int(x) % 2 == 0:
            Even_num.append(x)
        else:
            Odd_num.append(x)
    
    filter_list = Lowerletters + Upperletters + Odd_num + Even_num
    for x in filter_list:
        ginort += x
    
    
    
    return ginort

if __name__ == "__main__":
    S = 'Sorting1234'
    result = ginortS(S)
    print(result)