#testint the attendece generator(not promoted this code as official)
print('hello')

class_list = ['1','2','3','4','5'] #total list
pres_list = [] #temperory list
abs_list = [] #final result list
list = []
x= 0   #<<<attendence counting var<<<
x = int(x) 

#main code comes...
print("type how many presentees are there: ") 
present1 = input()
present1 = int(present1)

for i in range(present1): #how many time presnt should define
    print("type the presentees: ")
    present = input()
    present = int(present)
    pres_list.append (present)

for a in range (5):
	if x+1 not in pres_list:
		abs_list.append (x+1)
		x = x + 1
	else: 
		list.append(x+1)
		x = x+1
print('the absentees are:')
print(abs_list)
input()