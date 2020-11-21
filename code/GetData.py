data = open('../Data.txt', 'r')
Archery = open('../data/archery.txt', 'w+')
Diving10 = open('../data/diving10.txt', 'w+')
Volleyball = open('../data/volleyball.txt', 'w+')
Hockey = open('../data/hockey.txt', 'w+')
Gymnastics = open('../data/gymnastics.txt', 'w+')
Diving3 = open('../data/diving3.txt', 'w+')


contents = data.readlines()
for x in contents:
	temp = x.split()
	if(temp[2] == "Archery"):
		Archery.write(x)
	if(temp[2] == "Aquatics"):
		if(temp[3] == "Diving"):
			if(temp[4] == "3m"):
				Diving3.write(x)
			if(temp[4] == "10m"):
				Diving10.write(x)
	if(temp[2] == "Volleyball"):
		Volleyball.write(x)
	if(temp[2] == "Hockey"):
		Hockey.write(x)
	if(temp[2] == "Gymnastics"):
		if(temp[5] == "floor"):
			Gymnastics.write(x)
	print(temp[2])

