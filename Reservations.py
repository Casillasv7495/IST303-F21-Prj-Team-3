global f
f = 0

#this t_service function is used to select service name
def t_service():
	global f
	f = f+1
	print("what service do you want?")
	print("1,service 1 ")
	print("2,service 2 ")
	print("3,service 3")
	print("4,back")
	service = int(input("choose your service: "))
	if service == 4:
	# in this it goes to room function and from room it goes to service function and it comes back here and then go to location
	    room()
	    location()
	    return 0
	if f == 1:
	    location()

# this location function used to select screen
def location():
	print("which place do you want to do service: ")
	print("1,place 1")
	print("2,place 2")
	print("3,place 3")
	a = int(input("choose your place: "))
	slot = int(input("number of slot do you want?: "))
	timing(a)

# this timing function used to select timing for movie
def timing(a):
	time1 = {
		"1": "10.00-1.00",
		"2": "1.10-4.10",
		"3": "4.20-7.20",
		"4": "7.30-10.30"
	}
	time2 = {
		"1": "10.15-1.15",
		"2": "1.25-4.25",
		"3": "4.35-7.35",
		"4": "7.45-10.45"
	}
	time3 = {
		"1": "10.30-1.30",
		"2": "1.40-4.40",
		"3": "4.50-7.50",
		"4": "8.00-10.45"
	}
	if a == 1:
		print("choose your time:")
		print(time1)
		t = input("select your time:")
		x = time1[t]
		print("successfull!, enjoy movie at "+x)
	elif a == 2:
		print("choose your time:")
		print(time2)
		t = input("select your time:")
		x = time2[t]
		print("successfull!, enjoy movie at "+x)
	elif a == 3:
		print("choose your time:")
		print(time3)
		t = input("select your time:")
		x = time3[t]
		print("successfull!, enjoy movie at "+x)
	return 0


def service(location):
	if location == 1:
		t_service()
	elif location == 2:
		t_service()
	elif location == 3:
		t_service()
	elif location == 4:
		city()
	else:
		print("wrong choice")


def room():
	print("which location do you wish to do service? ")
	print("1,candy")
	print("2,chocolate")
	print("3,strawberry")
	print("4,back")
	a = int(input("choose your option: "))
	service(a)
	return 0

# this function is used to select city
def city():
	print("Hi welcome to service slot booking: ")
	print("where you want to do the service?:")
	print("1,city 1")
	print("2,city 2 ")
	print("3,city 3 ")
	place = int(input("choose your option: "))
	if place == 1:
	    room()
	elif place == 2:
	    room()
	elif place == 3:
	    room()
	else:
	    print("wrong choice")


city() # it calls the function city
