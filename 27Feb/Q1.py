def char(string):
    for i in range(len(string)):
        if i % 2 == 0:
            print(string[i])

char("abcd")