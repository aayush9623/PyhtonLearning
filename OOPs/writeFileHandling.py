f= open('MyData','r')
#overwrite file always
f1 = open('abc','w')
#appending
f1.open('abc','a')
f1.write("something")
f1.write("New")