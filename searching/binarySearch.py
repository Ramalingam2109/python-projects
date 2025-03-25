# procedure
# makes sure the given list is sorted
# assign the first element as lower bound as the last element as upper bound
# calculate the mid value and check if it is equal to the searching element
# if yes return true
# else check whether mid value > or < the searching element


lst = [4,7,8,12,45,99]

searching_element = 45
pos = -1
# sorting the list
def binary_search(lst, searching_element):
    l = 0
    u = len(lst)-1
    while l <= u:
        mid = (l +u)//2
        if lst[mid] ==searching_element:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < searching_element:
                l = mid+1
            elif lst[mid] > searching_element:
                u = mid-1
    return False



if binary_search(lst,searching_element):
    print(f"{searching_element} found at {pos}")
else:
    print(f"The given element is not in the sequence")