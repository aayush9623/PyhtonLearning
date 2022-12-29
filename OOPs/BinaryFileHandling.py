#read binary
f = open('Capture.JPG','rb')
#writw binary
f1 = open('Capture1.JPG','wb')
for i in f:
    f1.write(i)