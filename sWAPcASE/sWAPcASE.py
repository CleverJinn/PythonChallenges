from unittest import result


def swap_case(s):
    s_list = list(s)
    filter_list = []
    s_swaped = ""
    
    for x in s_list:
        if x.isalpha():
            if x.isupper():
                x = x.lower()
                filter_list.append(x)
                             
            elif x.islower():
                x = x.upper()
                filter_list.append(x)
        else:
            filter_list.append(x)
            
    for x in filter_list:
        s_swaped += x
             
    return s_swaped

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)