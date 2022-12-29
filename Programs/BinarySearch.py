List1 = [1, 2, 6, 7, 8, 10, 27, 63, 73, 94]
num = 65
pos =-1
def searchBinary(List1,num):
    L = 0
    U = int(len(List1)-1)
    while L <= U:
        Mid = int((L + U) // 2)
        if List1[Mid] == num:
            globals()['pos'] = Mid
            return True
        else:
            if int(List1[Mid]) > int(num):
                U = Mid-1
            else:
                L = Mid+1

    return False


if searchBinary(List1,num):
    print("Found at ",pos+1)
else:
    print("Not Found")

