from collections import Counter
i = int(input("Enter your square root: "))
tnl = [] #list composed of dividends and final undividable remainder. This is the reference list for the other two lists.
snl = [] #list composed of numbers that did not have any duplicate values, or the reminants of the numbers who's total number of duplicates was odd.
wnl = [] #list of numbers who's number of duplicates was even.

def listmult(list):
    LstLen = len(list)
    for num in range(LstLen):
        if len(list) == 1:
            break
        else:
            list[0] *= list[1]
            del list[1]

for x in range(10):
    if i == 1:
        break
    elif i%2 == 0:
        i /= 2
        tnl.append(2)
        continue
    elif i%3 == 0:
        i /= 3
        tnl.append(3)
        continue
    elif i%5 == 0:
        i /= 5
        tnl.append(5)
        continue
    else:
        tnl.append(i)
        break
    break

nd = Counter(tnl)
for num in nd:
    x = (nd[num])
    if x == 1:
        snl.append(num)
    elif x%2 != 0:
        x -= 1
        snl.append(num)
        x =int(x/2)
        for z in range(x):
            wnl.append(num)
    elif x%2 == 0:
        x = int(x/2)
        for z in range(x):
            wnl.append(num)

listmult(snl)
listmult(wnl)
print("Your simplified root is {} square root of {}".format(wnl,snl))
