
pos = -1
#while loop
def search(list,n):
    i=0
    while i < len(list):
        if list[i]==n:
            globals()['pos'] = i
            return True
            break
        i += 1
    return False
#for loop
def searchFor(list,n):
    i = 0
    for i in list:
        if i==n:
            globals()['pos'] = list.index(i)
            return True
            break
    return False

list = [9,3,3,2,7,2,8,2,5,4]
n=7

if searchFor(list,n):
    print("Found at ",pos+1)
else:
    print("Not Found")