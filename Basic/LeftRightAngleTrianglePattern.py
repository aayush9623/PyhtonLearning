for j in range(1,5):
    print("# "*j)
print()
################### OR #######################
for j in range(1,5):
    for j in range(j):
        print("# ", end="")
    print()

################### Reverse triangle #######################
print()
for j in range(4):
    for j in range(4-j):
        print("# ", end="")
    print()

################### equilateral triangle #######################

print()
n=15
for i in range(1,11):
    print(' '*(n-i) + "* "*i)