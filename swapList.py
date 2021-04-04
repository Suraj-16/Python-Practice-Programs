

list1 = [1,2,3,4,5,6]   

def swapList(list1):
    size = len(list1)
    temp = list1[0]
    list1[0] = list1[size - 1]
    list1[size - 1] = temp
    return list1

print(swapList(list1))    