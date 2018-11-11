
def load(name):
	data = []
	filename = name + '.jrl'
	
	with open(filename, 'r') as fin:
		for entry in fin.readlines():
			data.append(entry.rstrip())
	return data


def save(name, journal_data):
	
	filename = 'name.jrl'
	
	with open(filename, 'w') as fout:
	
		for entry in journal_data:
			fout.write(entry +'\n')


def add_entry(text, journal_data):
	journal_data.append(text)
	
