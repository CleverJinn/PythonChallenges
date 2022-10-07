def count_substring(string, substring):
    results = 0;
    sub_len = len(substring)
    for i in range(len(string)):
        if string[i:i+sub_len] == substring:
            results += 1
    return results

if __name__ == '__main__':
    count = count_substring('ABCDCDC', 'CDC')
    print(count)