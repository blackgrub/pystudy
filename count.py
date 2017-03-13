def count_to(x):
    """ Counts to a number """
    count = 0
    while count <= x:
        print(count)
        count += 1


count_to(int(input("Input a number: ")))
