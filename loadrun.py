'''loadrun.py'''
'''11 Jul 2015'''
'''owner Supot Sawangpiriyakij'''
'''one and only version'''
global program_text
program_text=[]
def load(file_name):
	global program_text
	program_text = ''
	f=open(file_name,'r')
	read_text = f.readlines()
	for line in read_text:
		program_text.append(line)							
	f.close()
def run():
	global program_text
	j = ''
	for i in program_text:
		if type(i) is str:
			j = j + i + '\n'
	if (j != ''):
		exec(j + '\n')
		j = ''
