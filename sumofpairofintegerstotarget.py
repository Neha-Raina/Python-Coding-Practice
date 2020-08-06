def pairofintegers(list1,target):
    lo = 0
    hi = len(list1)-1
    while lo<hi:
        if list1[lo] + list1[hi] == target:
            return list1[lo],list1[hi]
        elif list1[lo] + list1[hi] > target:
            hi-=1
        elif list1[lo] + list1[hi] < target:
            lo+=1
    return ()

if __name__ == '__main__':
    list1 = []
    target = int(input('Enter the target number: '))
    lenoflist = int(input('Enter the length of list: '))
    for i in range(lenoflist):
        user_input = int(input('Enter the ' + str(i + 1) + ' number: '))
        list1.append(user_input)
    list1.sort()
    result = pairofintegers(list1, target)
    if result == ():
        print("No pair exist within the list whose sum is equal to target")
    else:
        print('The two nums that add up to target are: ', result)
