import datetime
print datetime.datetime.now()

from random import randint
mylist = []

for times in range(0,100):
	number = (randint(0, 10000))
	mylist.append(number)

for idx in range(len(mylist)-1):
	for idx2 in range(len(mylist)-1):
		if mylist[idx2]>mylist[idx2+1]:
			temp = mylist[idx2]
			mylist[idx2] = mylist[idx2+1]
			mylist[idx2+1] = temp
print mylist

print datetime.datetime.now()
