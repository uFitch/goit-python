from datetime import datetime, date


def congratulate(users):
	birthday_people = [
						{'Monday:':[]}, 
						{'Tuesday:':[]}, 
						{'Wednesday:':[]}, 
						{'Thursday:':[]},
						{'Friday:':[]}
						]
	for elem in users:
		elem['birthday'] = elem['birthday'].replace(year=date.today().year)

	birthday_people[0]['Monday:'] = [elem['name'] for elem in users
		if elem['birthday'].isocalendar()[1] == date.today().isocalendar()[1] and 
		elem['birthday'].isocalendar()[2] == 6 or 
		elem['birthday'].isocalendar()[1] == date.today().isocalendar()[1] + 1
		and elem['birthday'].isocalendar()[2] == 1 or
		elem['birthday'].isocalendar()[1] == date.today().isocalendar()[1] and 
		elem['birthday'].isocalendar()[2] == 7]

	birthday_people[1]['Tuesday:'] = [elem['name'] for elem in users
		if elem['birthday'].isocalendar()[1] == date.today().isocalendar()[1] + 1
		and elem['birthday'].isocalendar()[2] == 2]

	birthday_people[2]['Wednesday:'] = [elem['name'] for elem in users
		if elem['birthday'].isocalendar()[1] == date.today().isocalendar()[1] + 1
		and elem['birthday'].isocalendar()[2] == 3]

	birthday_people[3]['Thursday:'] = [elem['name'] for elem in users
		if elem['birthday'].isocalendar()[1] == date.today().isocalendar()[1] + 1
		and elem['birthday'].isocalendar()[2] == 4]

	birthday_people[4]['Friday:'] = [elem['name'] for elem in users
		if elem['birthday'].isocalendar()[1] == date.today().isocalendar()[1] + 1
		and elem['birthday'].isocalendar()[2] == 5]

	for elem in birthday_people:
		for key, value in elem.items():
			if value:
				print(f'{key} {", ".join(value)}')