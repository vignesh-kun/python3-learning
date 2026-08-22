# Attendence generator version 3.0 official code.
#note: -----------
#copy rights only to k.vignesh, athestic creations...(^^^plz dont copy!!!^^^)

#hello user!!!
print('')
print('')
print('')
print('						Athestic Creations')
print('					 	    presents')
print('')
print('')
print('')
input('press enter key to continue...')
print('')
print('						Attendence Generator')
print('				 	   	   version.3.1.1')
input('press enter key to continue...')
print('')
print('hello, user !!!')
print('Welcome to attendence taker_version 3.x :)')


#all lists (lists)
class_list = [			'1', 	'2', 	'3', 		'4', 		'5', 	    '6', 		'7', 		'8', 		'9', 		'10', 		'11', 			'12', 		  '13', 	'14', 		'15',			 '16', 				'17',	 '18', 	'19', 		'20', 		 '21', 	'22', 	'23', 	    	'24', 		'25', 	'26', 			'27', 	'28', 		'29', 		'30', 		 '31', 		'32', 		'33', 	   '34',   '35', 	'36',		'37', 	  '38', 	'39', 		'40', 		'41', 	'42', 			'43', 	  '44', 		'45', 		'46'] #total list
class_str_list = ['abhigna', 'aditi', 'ankitha', 'hansika', 'keerthana', 'lakshmi', 'mary_neha', 'mary_siri', 'nischala', 'pranavi', 'sai_nipuna', 'siri_chandana', 'sowmya', 'sruthika', 'p_vaishnavi', 'k_vaishnavi', 'v_vaishnavi', 'akhil', 'akshit', 'anirudh', 'ankit', 'aswin', 'bhavishya', 'bhuvanesh', 'dwipadh', 'abhinav', 'kawstubh', 'krishna', 'navneeth', 'pranesh', 'ritish', 'sreenivas', 'samarth', 'satya', 'shane', 'siddha', 'sri_charan', 'srikar', 'susyamal', 'tapan', 'vignesh', 'viswaroop', 'yashaswin', 'prateek', 'mahindra', 'koushika']
pres_list = [] #temperory list
abs_list = [] #final result list
list = []

#^main role playing variables..^
x= -1   #<<<attendence counting var<<<
x = int(x) 

#main code comes...
print('')
print('')
print("Type how many presentees are there: ") 
present1 = input()
present1 = int(present1)

# preentees inputs...
for i in range(present1): #how many time presnt should define
    print("type the presentees: ")
    present = input()
    present = str(present)
    pres_list.append (present)

#main code/ : list preparing...
for a in range (46):
	if class_str_list[x+1] not in pres_list:
		abs_list.append (class_list[x+1])
		x = x + 1
	else: 
		list.append(x+1)
		x = x+1

#MAIN CODE done!...now displaying absentees...
print('')
print('generating absentees...')
input('...')
input('press enter key to continue !!!')
print('')
print('The absentees are:')
print(abs_list)
print('')
print('')
input('press enter key to continue...')

print('Hope you enjoy my attendence generator :)')
print('thank you...for your valuable time spending to use this program :)')
print('')
print('								----------x----------')
print('')
input('press enter key to exit...')
#updates for this program are there...this is the stable verion of attendence taker 3.x
#updates conformed ...!!!!
#									----------x----------
#secret reveal: In next 3.1 update :
#	im going to give the feature of getting control on absentees in letters and numbers