marks = [95,74,83, 94,56,16,46]
print(marks)
#indexing starts from one
print(marks[2])
# - indexing starts from end
print(marks[-2])
# print range of list
print(marks[1:3])

for score in marks:
    print(score)

##append
marks.append(99)
print(marks)
# insert at index
marks.insert(0,99)

#find item in list
print( 99 in marks)


#length of marks list
print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1


#empty the list
print(marks.clear())

# tuple are immutable
marks1= (96,34,25,16,96,86,87,96,96)
print(marks1.count(96))
print(marks1.index(34))


#sets
# no suplicates
# no indexing
# unordered
marks2= {6,34,25,16,96,86,87,96,96}
print(marks2)

#dictonary
marks3 = {"english": 85,"chemistry":86}
print(marks3["chemistry"])
#insert
marks3["physics"] =  87
print(marks3)
marks3["chemistry"] =  98
print(marks3)