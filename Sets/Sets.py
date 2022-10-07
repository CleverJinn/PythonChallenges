from unittest import result


def average(array):
    array = set(array)
    array_avg = (sum(array)/len(array))
    return round(array_avg,3)

if __name__ == '__main__':
    n = 10
    arr = [161,182,161,154,176,170,167,171,170,174]
    result = average(arr)
    print(result)