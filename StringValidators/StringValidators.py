from curses.ascii import isalnum, isalpha, isdigit


if __name__ == '__main__':
    s = "#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
    flag0 = 'False'
    flag1 = 'False'
    flag2 = 'False'
    flag3 = 'False'
    flag4 = 'False'
    for x in s:
        if x.isalnum():
            flag0 = 'True'
        if x.isalpha():
            flag1 = 'True'
        if x.isdigit():
            flag2 = 'True'
        if x.islower():
            flag3 = 'True'
        if x.isupper():
            flag4 = 'True'     
    print(flag0)
    print(flag1)
    print(flag2)
    print(flag3)
    print(flag4)