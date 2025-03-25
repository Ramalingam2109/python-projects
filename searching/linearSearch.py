lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
searching_element = 1
pos = -1


def search(lst,n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i+1
            return True
        i = i + 1
        pass
    return False

    pass


if search(lst,searching_element):
    print("Value found at",pos)
    pass
else:
    print("Value not inside the sequence")
