from StudentMenu import menu
from StudentInsert import insertrecords
from StudentViews import studentview, studentviews
from StudentSearch import studentsearch
while(True):
	menu()
	try:
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1:
				insertrecords()
			case 2:
				studentview()
			case 3:
				studentviews()
			case 4:
				studentsearch()
			case 5:
				print("Thx for Using Program")
				break
			case _:
				print("Ur Selection of Operation is wrong--try again")
	except ValueError:
		print("Don't enter strs , symbols and alnums for Choice--try again")
