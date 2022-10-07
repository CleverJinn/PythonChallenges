def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s_new = mutate_string('abracadabra', 5, 'k')
    print(s_new)